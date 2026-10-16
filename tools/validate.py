#!/usr/bin/env python3
"""Offline evidence integrity and local-document-link checks."""
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'observed-page', 'manufacturer-claim', 'interview-claim', 'reported-claim',
            'reported-observation', 'reported-interview', 'conflicting-reports',
            'historical-claim', 'patent-disclosure', 'unknown'}
ACCESS = {'browser-read', 'transcript-read', 'metadata-only', 'indexed', 'indexed-stale',
          'full-text', 'blocked', 'linked-only'}


def load(name):
    return json.loads((ROOT / 'data' / f'{name}.json').read_text())


def validate():
    errors = []
    sources, claims, events, meta = (load(n) for n in ('sources', 'claims', 'timeline', 'meta'))
    cutoff = dt.date.fromisoformat(meta['cutoff'])
    ids = {s['id'] for s in sources}
    for rows, prefix, required in (
        (sources, 'S', {'id', 'title', 'publisher', 'url', 'kind', 'access', 'support', 'limitations', 'checked', 'published'}),
        (claims, 'C', {'id', 'topic', 'era', 'status', 'statement', 'sources', 'scope', 'unresolved', 'checked'}),
    ):
        seen = set()
        for row in rows:
            ident = row.get('id', '?')
            if required - row.keys():
                errors.append(f'{ident}: missing {sorted(required-row.keys())}')
                continue
            if ident in seen or not re.fullmatch(prefix + r'\d{2,}', ident):
                errors.append(f'Invalid or duplicate ID: {ident}')
            seen.add(ident)
            for key in required - {'published'}:
                if not row[key]:
                    errors.append(f'{ident}: empty {key}')
            try:
                if dt.date.fromisoformat(row['checked']) > cutoff:
                    errors.append(f'{ident}: checked after edition cutoff')
            except (TypeError, ValueError):
                errors.append(f'{ident}: invalid checked date')
    for source in sources:
        if source['access'] not in ACCESS:
            errors.append(f"{source['id']}: invalid access")
        url = urlsplit(source['url'])
        if url.scheme != 'https' or not url.netloc or url.username or url.password:
            errors.append(f"{source['id']}: source must use credential-free HTTPS")
        if source['published']:
            try:
                if dt.date.fromisoformat(source['published']) > cutoff:
                    errors.append(f"{source['id']}: future publication")
            except ValueError:
                errors.append(f"{source['id']}: invalid publication date")
    source_map = {s['id']: s for s in sources}
    for row in claims + events:
        label = row.get('id', row.get('title', '?'))
        if not row.get('sources') or set(row['sources']) - ids:
            errors.append(f'{label}: missing or unresolved source IDs')
    for claim in claims:
        if claim['status'] not in STATUSES:
            errors.append(f"{claim['id']}: invalid status")
        if claim['status'] in {'observed-page', 'manufacturer-claim', 'interview-claim'}:
            usable = [source_map[s]['access'] in {'browser-read', 'transcript-read', 'full-text'}
                      for s in claim['sources'] if s in source_map]
            if not any(usable):
                errors.append(f"{claim['id']}: direct claim lacks directly reviewed evidence")
        if claim['era'] == '2017' and claim['status'] != 'historical-claim':
            errors.append(f"{claim['id']}: legacy concept must remain historical")
    for event in events:
        try:
            date = event['date']
            if not re.fullmatch(r'\d{4}(?:-\d{2})?(?:-\d{2})?', date):
                raise ValueError
            normalized = date + {4: '-01-01', 7: '-01', 10: ''}[len(date)]
            if dt.date.fromisoformat(normalized) > cutoff and event['kind'] != 'target':
                errors.append(f"{event['title']}: future event must be a target")
        except (KeyError, ValueError):
            errors.append(f"{event.get('title')}: invalid event date")
    for file in ROOT.rglob('*.md'):
        if '.git' in file.parts or 'dist' in file.parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            link = link.strip('<>')
            if urlsplit(link).scheme or link.startswith('#'):
                continue
            path = unquote(urlsplit(link).path)
            if path and not (file.parent / path).exists():
                errors.append(f'{file.relative_to(ROOT)}: broken local link {link}')
    return errors


if __name__ == '__main__':
    issues = validate()
    if issues:
        print('\n'.join(issues))
        raise SystemExit(1)
    print(f"Validated {len(load('sources'))} sources, {len(load('claims'))} claims, {len(load('timeline'))} timeline events and local Markdown links.")
