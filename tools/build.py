#!/usr/bin/env python3
"""Deterministically build reference tables and a dependency-free static explorer."""
import argparse
import html
import json
from pathlib import Path
import re
import shutil
import datetime as dt
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site' / 'dist'


def load(name):
    return json.loads((ROOT / 'data' / f'{name}.json').read_text())


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def reference_docs():
    sources, claims, events = (load(n) for n in ('sources', 'claims', 'timeline'))
    by_id = {s['id']: s for s in sources}

    def refs(ids):
        return ' · '.join(f"[{i}]({by_id[i]['url']})" for i in ids)

    text = '# Claim ledger\n\n[Home](../README.md) · [Evidence labels](../research/methodology.md)\n\n'
    text += f"Generated from `data/claims.json`. Checked through {load('meta')['cutoff']}. Status describes evidence, not a guarantee.\n\n"
    for claim in claims:
        text += f"## {claim['id']} — {claim['topic']}\n\n**{claim['status']} · {claim['era']}**\n\n{claim['statement']}\n\n"
        text += f"Scope: {claim['scope']}\n\nSources: {refs(claim['sources'])}\n\n"
        if claim.get('locator'):
            text += f"Locator: {claim['locator']}\n\n"
        text += f"Unresolved: {claim['unresolved']}\n\n"
    result = {'docs/claims.md': text}
    text = '# Annotated source library\n\n[Home](../README.md) · [Method and access limits](../research/methodology.md)\n\n'
    text += f'{len(sources)} retained source records. This count includes incomplete access and research leads; it is not a count of fully verified documents.\n\n'
    for source in sources:
        text += f"## {source['id']} — {source['title']}\n\n[{source['publisher']}]({source['url']})\n\n"
        text += f"Type: {source['kind']} · Access: **{source['access']}** · Published: {source['published'] or 'not established'} · Checked: {source['checked']}\n\n"
        text += f"Supports: {source['support']}\n\nLimits: {source['limitations']}\n\n"
    result['docs/sources.md'] = text
    text = '# News and development timeline\n\n[Home](../README.md) · [Sources](sources.md)\n\n'
    text += 'Selected milestones, not every announcement. Dates preserve known precision. Future entries are targets.\n\n'
    text += '| Date | Kind | Milestone | Evidence |\n|---|---|---|---|\n'
    for event in sorted(events, key=lambda e: e['date']):
        text += f"| {event['date']} | {event['kind']} | **{cell(event['title'])}** — {cell(event['summary'])} | {refs(event['sources'])} |\n"
    result['docs/timeline.md'] = text
    audit = load('audit')
    text = '# Record-by-record audit\n\n[Home](../README.md) · [Findings and limits](../research/audit.md)\n\n'
    text += f"Reviewed {audit['reviewed_on']}. A supported attribution is not independent validation of a car.\n\n"
    text += '## Sources\n\n| ID | Outcome | Method and locator | Finding |\n|---|---|---|---|\n'
    for review in audit['sources']:
        text += f"| [{review['source_id']}]({by_id[review['source_id']]['url']}) | {review['verdict']} | {cell(review['method'])}: {cell(review['locator'])} | {cell(review['note'])} |\n"
    text += '\n## Claims\n\n| Claim | Outcome | Checked location |\n|---|---|---|\n'
    for review in audit['claims']:
        text += f"| {review['claim_id']} | {review['verdict']} | {cell(review['locator'])} |\n"
    text += '\n## Timeline\n\n| Event | Outcome | Sources |\n|---|---|---|\n'
    for review in audit['timeline']:
        text += f"| {cell(review['event'])} | {review['verdict']} | {cell(review['locator'])} |\n"
    result['docs/audit-ledger.md'] = text
    return {name: text.rstrip() + '\n' for name, text in result.items()}


def destination(url, source_file):
    parts = urlsplit(url)
    if parts.netloc and not parts.scheme:
        return 'https:' + url
    if parts.scheme:
        return url if parts.scheme in {'https', 'http'} else '#'
    if not parts.path:
        return url
    target = (source_file.parent / unquote(parts.path)).resolve()
    if not target.is_relative_to(ROOT.resolve()):
        raise ValueError(f'Local link escapes the repository: {url}')
    if target.suffix == '.md':
        relative = target.relative_to(ROOT.resolve()).as_posix()
        if relative == 'README.md':
            return f"{load('meta')['repository']}/blob/main/README.md#{parts.fragment}" if parts.fragment else 'index.html'
        return page_name(relative) + (f'#{parts.fragment}' if parts.fragment else '')
    if target.name == 'banner.svg':
        return 'banner.svg'
    relative = target.relative_to(ROOT.resolve()).as_posix()
    return f"{load('meta')['repository']}/blob/main/{quote(relative)}" + (f'#{parts.fragment}' if parts.fragment else '')


def page_name(relative):
    return 'guide-' + relative.replace('/', '-').removesuffix('.md') + '.html'


def validate_site(directory):
    class Document(HTMLParser):
        def __init__(self):
            super().__init__()
            self.links, self.ids = [], set()

        def handle_starttag(self, tag, attrs):
            attributes = dict(attrs)
            if 'id' in attributes:
                self.ids.add(attributes['id'])
            for name in ('href', 'src'):
                if name in attributes:
                    self.links.append(attributes[name])

    pages = {}
    for path in directory.glob('*.html'):
        document = Document()
        document.feed(path.read_text(encoding='utf-8'))
        pages[path.name] = document
    errors = []
    for name, document in pages.items():
        for link in document.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = unquote(parts.path) or name
            if not (directory/target).is_file():
                errors.append(f'{name}: missing generated target {link}')
            elif parts.fragment and target in pages and parts.fragment not in pages[target].ids:
                errors.append(f'{name}: missing generated anchor {link}')
    return errors


def remove_obsolete_outputs(previous, current):
    for name in set(previous) - set(current):
        # Delete only an earlier manifest's generator-owned guide pages.
        if re.fullmatch(r'guide-[A-Za-z0-9_-]+\.html', name):
            (OUT/name).unlink(missing_ok=True)


def inline(text, source_file):
    # Only an intentionally small Markdown subset is supported; HTML is escaped.
    tokens = []

    def keep(value):
        tokens.append(value)
        return f'\x00{len(tokens)-1}\x00'

    def link(match):
        url = destination(match[2], source_file)
        return keep(f'<a href="{html.escape(url, quote=True)}">{html.escape(match[1])}</a>')

    text = re.sub(r'!?\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = re.sub(r'`([^`]+)`', lambda m: keep('<code>' + html.escape(m[1]) + '</code>'), text)
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m[1])], text)


def markdown(text, source_file):
    lines, result, i = text.splitlines(), [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('```'):
            language = line[3:]
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(lines[i])
                i += 1
            if language == 'mermaid':
                chapter = source_file.resolve().relative_to(ROOT.resolve()).as_posix()
                url = f"{load('meta')['repository']}/blob/main/{quote(chapter)}"
                result.append('<p class="caption"><a href="' + html.escape(url, quote=True) + '">View the rendered diagram on GitHub</a>. Diagram source:</p><pre><code>' + html.escape('\n'.join(block)) + '</code></pre>')
            else:
                result.append('<pre><code>' + html.escape('\n'.join(block)) + '</code></pre>')
            i += 1
            continue
        heading = re.match(r'^(#{1,6}) (.*)', line)
        if heading:
            level, title = len(heading[1]), heading[2]
            anchor = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
            result.append(f'<h{level} id="{anchor}">{inline(title, source_file)}</h{level}>')
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                if not re.fullmatch(r'[| :\-]+', lines[i]):
                    rows.append([v.strip().replace('\\|', '|') for v in re.split(r'(?<!\\)\|', lines[i].strip('|'))])
                i += 1
            result.append('<p class="table-help caption">Scroll the table horizontally to read all columns.</p><div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable table"><table>')
            for n, row in enumerate(rows):
                tag = 'th' if n == 0 else 'td'
                result.append('<tr>' + ''.join(f'<{tag}>{inline(v, source_file)}</{tag}>' for v in row) + '</tr>')
            result.append('</table></div>')
            continue
        bullet = re.match(r'^(?:- |\d+\. )(.*)', line)
        if bullet:
            ordered = bool(re.match(r'^\d', line))
            tag = 'ol' if ordered else 'ul'
            result.append(f'<{tag}>')
            while i < len(lines):
                match = re.match(r'^(?:- |\d+\. )(.*)', lines[i])
                if not match:
                    break
                result.append('<li>' + inline(match[1], source_file) + '</li>')
                i += 1
            result.append(f'</{tag}>')
            continue
        result.append('<p>' + inline(line.removeprefix('> '), source_file) + '</p>')
        i += 1
    return '\n'.join(result)


def shell(title, body, scripts=''):
    cutoff = dt.date.fromisoformat(load('meta')['cutoff']).strftime('%d %b %Y')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Independent Tesla Roadster learning guide: evidence, engineering, announcements, unknowns and reproducible physics.">
<title>{html.escape(title)} · Roadster Reference</title><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="top"><a class="brand" href="index.html">R<span>R</span> <b>Roadster Reference</b></a>
<nav aria-label="Main navigation"><a href="index.html#learn">Learn</a><a href="index.html#claims">Evidence</a><a href="index.html#sources">Sources</a><a href="index.html#lab">Physics lab</a><a href="{load('meta')['repository']}">GitHub</a></nav></header>
{body}<footer><p>Independent education. No affiliation with Tesla or SpaceX.</p><p>Research cutoff <strong>{cutoff}</strong> · <a href="guide-research-methodology.html">Method & limits</a> · <a href="guide-CONTRIBUTING.html">Contribute</a> · MIT project content; external rights retained.</p></footer>{scripts}</body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated Markdown without writing')
    args = parser.parse_args()
    from validate import validate
    errors = validate(root=ROOT, check_links=False)
    if errors:
        raise SystemExit('\n'.join(errors))
    generated = reference_docs()
    if args.check:
        stale = [name for name, text in generated.items() if not (ROOT/name).exists() or (ROOT/name).read_text() != text]
        if stale:
            raise SystemExit('Stale generated docs: ' + ', '.join(stale))
        errors = validate(root=ROOT)
        if errors:
            raise SystemExit('\n'.join(errors))
        print('Generated Markdown is current.')
        return
    for name, text in generated.items():
        (ROOT/name).write_text(text)
    errors = validate(root=ROOT)
    if errors:
        raise SystemExit('\n'.join(errors))
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = OUT/'build-manifest.json'
    previous = json.loads(manifest.read_text()) if manifest.exists() else []
    current = ['index.html', 'style.css', 'app.js', 'banner.svg']
    for name in ('style.css', 'app.js'):
        shutil.copyfile(ROOT/'site'/name, OUT/name)
    shutil.copyfile(ROOT/'assets'/'banner.svg', OUT/'banner.svg')
    data = {name: load(name) for name in ('sources', 'claims', 'timeline', 'meta')}
    body = (ROOT/'site'/'index.template.html').read_text()
    body = body.replace('{{cutoff_display}}', dt.date.fromisoformat(data['meta']['cutoff']).strftime('%d %B %Y'))
    for name in ('sources', 'claims', 'timeline'):
        body = body.replace('{{' + name + '_count}}', str(len(data[name])))
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    scripts = f'<script id="research-data" type="application/json">{payload}</script><script src="app.js" defer></script>'
    (OUT/'index.html').write_text(shell('Understand the new Roadster', body, scripts))
    pages = sorted((ROOT/'docs').glob('*.md')) + sorted((ROOT/'research').glob('*.md')) + [ROOT/'CONTRIBUTING.md', ROOT/'THIRD_PARTY_NOTICES.md']
    for path in pages:
        title = next((line[2:] for line in path.read_text().splitlines() if line.startswith('# ')), path.stem)
        content = markdown(path.read_text(), path)
        name = page_name(path.relative_to(ROOT).as_posix())
        (OUT/name).write_text(shell(title, '<main id="main" class="article">'+content+'</main>'))
        current.append(name)
    remove_obsolete_outputs(previous, current)
    manifest.write_text(json.dumps(sorted(current), indent=2)+'\n')
    errors = validate_site(OUT)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Built {len(pages)+1} HTML pages at {OUT}')


if __name__ == '__main__':
    main()
