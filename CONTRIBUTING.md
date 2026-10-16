# Contributing

Useful contributions improve understanding or evidence quality. A small sourced correction is more valuable than another unsourced specification list.

## Add or correct a claim

1. Search the existing claim and source IDs first.
2. Add the source to `data/sources.json` with a stable URL, publisher, date when known, checked date, access level, support and limitations.
3. Update `data/claims.json`. Specify era, configuration, evidence status and unresolved questions. Include a section or timestamp in `locator` when available.
4. Add a dated event to `data/timeline.json` only if it adds a useful milestone. Future dates must remain targets.
5. Review the changed records against the actual sources. Update their entries in `data/audit.json` with the method, precise locator, outcome and limitations. Compute each `record_sha256` using `tools/validate.py`'s `record_hash(record)` only after review; rehashing alone is not verification. Keep incomplete access explicit.
6. Run the commands below and include what changed in your pull request.

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/build.py
```

`docs/claims.md`, `docs/sources.md`, `docs/timeline.md` and `docs/audit-ledger.md` are generated; edit the JSON instead. Check in regenerated Markdown, but not `site/dist/`. Run `python3 tools/build.py --check` to check freshness. The optional HTTP probe (`python3 tools/check_sources.py --help`) does not replace reading the source.

## Editorial requirements

Prefer attributable primary evidence. Separate a company claim from an independent measurement. Keep old promises in their historical context. Do not infer vehicle fitment from a patent. Do not describe a reservation payment as retail price. Define rollout and units before comparing acceleration. Use `unknown` when evidence is insufficient.

Do not copy full articles, transcripts or proprietary manuals, upload Tesla firmware, include personal reservation/account information, or submit unlicensed imagery. Link external material and write concise original summaries. Document the rights to any new asset.

## Review and conduct

Discuss evidence and engineering respectfully. Do not impersonate Tesla or claim endorsement. Maintainers can decline unsupported assertions, spam, affiliate promotion, personal attacks or material with unclear rights. There is no guaranteed review time.

Maintainer: [fhajjej-ship-it](https://github.com/fhajjej-ship-it). Contributors retain copyright to their work and contribute under the project’s MIT license. The project does not require assignment of third-party rights you do not own.
