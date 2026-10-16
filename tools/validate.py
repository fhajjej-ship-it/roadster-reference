#!/usr/bin/env python3
"""Offline schema, evidence-review and local-link validation; no network requests."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'observed-page', 'manufacturer-claim', 'interview-claim', 'reported-claim',
            'reported-observation', 'reported-interview', 'conflicting-reports',
            'historical-claim', 'patent-disclosure', 'unknown'}
ACCESS = {'browser-read', 'transcript-read', 'metadata-only', 'indexed', 'indexed-stale',
          'full-text', 'document-read', 'blocked', 'linked-only'}
DIRECT = {'browser-read', 'transcript-read', 'full-text', 'document-read'}
KINDS = {'manufacturer', 'reporting', 'interview-report', 'interview', 'patent',
         'patent-index', 'engineering', 'regulator', 'manufacturer-context', 'filing'}
EVENT_KINDS = {'announcement', 'history', 'reveal', 'patent', 'target', 'observation'}
SOURCE_FIELDS = {'id', 'title', 'publisher', 'url', 'kind', 'access', 'support', 'limitations', 'checked', 'published'}
CLAIM_FIELDS = {'id', 'topic', 'era', 'status', 'statement', 'sources', 'scope', 'unresolved', 'checked'}
EVENT_FIELDS = {'date', 'title', 'summary', 'sources', 'kind'}


def load(name, root=ROOT):
    return json.loads((root / 'data' / f'{name}.json').read_text(encoding='utf-8'))


def record_hash(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def https_url(value):
    if not isinstance(value, str) or re.search(r'\s|[\x00-\x1f]', value):
        return False
    try:
        url = urlsplit(value)
        return bool(url.scheme == 'https' and url.hostname and not url.username and not url.password and url.port in (None, 443))
    except ValueError:
        return False


def date_value(value, *, partial=False):
    if not isinstance(value, str):
        raise ValueError('date must be a string')
    if partial:
        if not re.fullmatch(r'\d{4}(?:-\d{2})?(?:-\d{2})?', value):
            raise ValueError('invalid date precision')
        value += {4: '-01-01', 7: '-01', 10: ''}[len(value)]
    elif not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('invalid date format')
    return dt.date.fromisoformat(value)


def validate(root=ROOT, *, data=None, check_links=True, check_audit=True):
    errors = []
    if data is None:
        data = {}
        for name in ('meta', 'sources', 'claims', 'timeline', 'audit'):
            if name == 'audit' and not check_audit:
                continue
            try:
                data[name] = load(name, root)
            except (OSError, UnicodeError, json.JSONDecodeError) as error:
                errors.append(f'{name}: cannot read valid JSON ({type(error).__name__})')
    if not isinstance(data, dict):
        return ['data: expected an object']
    meta = data.get('meta')
    if not isinstance(meta, dict):
        return errors + ['meta: expected an object']
    try:
        cutoff = date_value(meta.get('cutoff'))
    except (TypeError, ValueError):
        return errors + ['meta: invalid cutoff']
    for key in ('title', 'version', 'scope'):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            errors.append(f'meta: invalid {key}')
    if not https_url(meta.get('repository')):
        errors.append('meta: repository must be credential-free HTTPS')

    valid = {}
    for name, prefix, required in (('sources', 'S', SOURCE_FIELDS), ('claims', 'C', CLAIM_FIELDS), ('timeline', None, EVENT_FIELDS)):
        rows = data.get(name)
        valid[name] = []
        if not isinstance(rows, list):
            errors.append(f'{name}: expected an array')
            continue
        seen = set()
        for index, row in enumerate(rows):
            label = f'{name}[{index}]'
            if not isinstance(row, dict):
                errors.append(f'{label}: expected an object')
                continue
            if required - row.keys():
                errors.append(f'{label}: missing {sorted(required-row.keys())}')
                continue
            identifier = row['id'] if prefix else row['date'] + ' / ' + row['title'] if isinstance(row['date'], str) and isinstance(row['title'], str) else None
            if not isinstance(identifier, str) or (prefix and not re.fullmatch(prefix+r'\d{2,}', identifier)):
                errors.append(f'{label}: invalid identifier')
                continue
            if identifier in seen:
                errors.append(f'{label}: duplicate identifier {identifier}')
                continue
            seen.add(identifier)
            label = identifier
            strings = required - {'sources', 'published'}
            bad = [key for key in strings if not isinstance(row[key], str) or not row[key].strip()]
            if bad:
                errors.append(f'{label}: invalid text fields {sorted(bad)}')
                continue
            if 'sources' in required and (not isinstance(row['sources'], list) or not row['sources'] or
                    any(not isinstance(item, str) for item in row['sources']) or len(set(row['sources'])) != len(row['sources'])):
                errors.append(f'{label}: sources must be a nonempty array of unique IDs')
                continue
            if prefix:
                try:
                    if date_value(row['checked']) > cutoff:
                        errors.append(f'{label}: checked after edition cutoff')
                except ValueError:
                    errors.append(f'{label}: invalid checked date')
            valid[name].append(row)

    source_map = {source['id']: source for source in valid['sources']}
    for source in valid['sources']:
        label = source['id']
        if source['access'] not in ACCESS or source['kind'] not in KINDS:
            errors.append(f'{label}: invalid source access or kind')
        if not https_url(source['url']):
            errors.append(f'{label}: source must use credential-free HTTPS')
        if source['published'] is not None:
            try:
                published = date_value(source['published'])
                if published > cutoff or published > date_value(source['checked']):
                    errors.append(f'{label}: publication after cutoff/check date')
            except (TypeError, ValueError):
                errors.append(f'{label}: invalid publication/check date')
    for row in valid['claims'] + valid['timeline']:
        label = row.get('id', row.get('title'))
        if set(row['sources']) - source_map.keys():
            errors.append(f'{label}: unresolved source IDs')
    for claim in valid['claims']:
        label = claim['id']
        if claim['status'] not in STATUSES or not re.fullmatch(r'\d{4}', claim['era']):
            errors.append(f'{label}: invalid status or era')
        evidence = [source_map[s] for s in claim['sources'] if s in source_map]
        if claim['status'] in {'observed-page', 'manufacturer-claim', 'interview-claim'}:
            owners = {'manufacturer', 'interview'} if claim['status'] != 'observed-page' else {'manufacturer'}
            if not any(s['access'] in DIRECT and s['kind'] in owners for s in evidence):
                errors.append(f'{label}: direct claim lacks a directly reviewed primary source')
        if claim['status'] == 'patent-disclosure' and not any(s['kind'] == 'patent' and s['access'] in DIRECT for s in evidence):
            errors.append(f'{label}: patent disclosure lacks reviewed patent text')
        if claim['era'] == '2017' and claim['status'] != 'historical-claim':
            errors.append(f'{label}: legacy concept must remain historical')
        if any(s['access'] in {'indexed-stale', 'blocked', 'linked-only'} for s in evidence):
            errors.append(f'{label}: inactive/unread source cannot support a current claim')
    for event in valid['timeline']:
        try:
            if event['kind'] not in EVENT_KINDS:
                errors.append(f"{event['title']}: invalid event kind")
            if date_value(event['date'], partial=True) > cutoff and event['kind'] != 'target':
                errors.append(f"{event['title']}: future event must be a target")
        except ValueError:
            errors.append(f"{event['title']}: invalid event date")

    if check_audit:
        audit = data.get('audit')
        if not isinstance(audit, dict):
            errors.append('audit: missing review ledger')
        else:
            for name, key in (('sources', 'source_id'), ('claims', 'claim_id'), ('timeline', 'event')):
                reviews = audit.get(name)
                if not isinstance(reviews, list) or any(not isinstance(r, dict) for r in reviews):
                    errors.append(f'audit: invalid {name} reviews')
                    continue
                keys = [r.get(key) for r in reviews]
                if any(not isinstance(k, str) for k in keys) or len(set(keys)) != len(keys):
                    errors.append(f'audit: invalid/duplicate {name} identifiers')
                    continue
                by_key = {r[key]: r for r in reviews}
                expected = set()
                for row in valid[name]:
                    identifier = row['id'] if name != 'timeline' else row['date']+' / '+row['title']
                    expected.add(identifier)
                    review = by_key.get(identifier, {})
                    if review.get('record_sha256') != record_hash(row):
                        errors.append(f'audit: missing/stale review of {identifier}')
                    if not all(isinstance(review.get(field), str) and review[field].strip() for field in ('verdict', 'method', 'locator', 'note')):
                        errors.append(f'audit: incomplete review of {identifier}')
                if set(by_key) - expected:
                    errors.append(f'audit: orphaned {name} reviews')
    if check_links:
        for file in root.rglob('*.md'):
            if '.git' in file.parts or 'dist' in file.parts:
                continue
            text = re.sub(r'```.*?```', '', file.read_text(encoding='utf-8'), flags=re.S)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                link = link.strip('<>')
                try:
                    parts = urlsplit(link)
                except ValueError:
                    errors.append(f'{file.relative_to(root)}: malformed link')
                    continue
                if parts.scheme or parts.netloc or link.startswith('#'):
                    continue
                path = unquote(parts.path)
                target = (file.parent / path).resolve()
                if not target.is_relative_to(root.resolve()) or (path and not target.exists()):
                    errors.append(f'{file.relative_to(root)}: broken/outside local link {link}')
    return errors


if __name__ == '__main__':
    issues = validate()
    if issues:
        print('\n'.join(issues))
        raise SystemExit(1)
    print(f"Validated {len(load('sources'))} sources, {len(load('claims'))} claims, {len(load('timeline'))} events, bound review receipts and local Markdown links.")
