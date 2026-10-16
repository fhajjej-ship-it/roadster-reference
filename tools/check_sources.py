#!/usr/bin/env python3
"""Optional HTTP access probe. A 200 response does not verify a source or claim."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import urllib.request

from validate import https_url, load

LIMIT = 6_000_000


def probe(source):
    result = dict(source_id=source['id'], requested_url=source['url'],
                  checked_at=datetime.now(timezone.utc).isoformat())
    if not https_url(source['url']):
        return {**result, 'error': 'InvalidSourceURL'}
    try:
        request = urllib.request.Request(source['url'], headers={
            'User-Agent': 'RoadsterReferenceResearch/0.1 (educational source access check)'})
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read(LIMIT+1)
            truncated = len(body) > LIMIT
            body = body[:LIMIT]
            result.update(http_status=response.status, resolved_url=response.url,
                          content_type=response.headers.get('Content-Type'),
                          bytes_read=len(body), truncated=truncated)
            result['prefix_sha256' if truncated else 'body_sha256'] = hashlib.sha256(body).hexdigest()
        if 'html' in (result['content_type'] or ''):
            match = re.search(r'<title[^>]*>(.*?)</title>', body.decode('utf-8', errors='replace'), re.I|re.S)
            if match:
                result['page_title'] = html.unescape(re.sub(r'\s+', ' ', match[1])).strip()
    except Exception as error:
        result.update(http_status=getattr(error, 'code', None), error=type(error).__name__)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Save access observations as JSON; defaults to stdout')
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(probe, load('sources')))
    report = dict(meaning='HTTP access observations only; not content verification, immutable archives or vehicle validation.',
                  results=results)
    text = json.dumps(report, indent=2, ensure_ascii=False)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
        print(f'Completed {len(results)} access probes; saved {args.output}')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
