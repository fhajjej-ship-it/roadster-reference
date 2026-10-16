# Repository audit — October 16, 2026

[Home](../README.md) · [Every source, claim and event](../docs/audit-ledger.md) · [Machine-readable review](../data/audit.json)

Initial scope: all 32 files in the first commit, 45 original source records, 33 original structured claims and 15 timeline entries, plus the additions made to correct this edition. Original baseline: `d37ada4bd81cd8228c4865286e24964e7e25c8fc`. The later [document follow-up](document-review.md) expanded this to 50 sources and 40 claims; the [payment-policy review](payment-policy-review.md) brings it to 52 sources and 42 claims. Review was performed by Codex with live source access and executable checks; it is not an independent human engineering certification.

## Evidence outcomes

The current registry contains **52 source records**. Of these, **49 support their stated scope**, **2 patent indexes remain limited to metadata**, and **1 obsolete citation is retired**. The previously unreadable agreement is now reviewed. Every record has an individual outcome, method, locator and note in the ledger. “Supported” means the cited source supports the attributed statement; it does not establish the car's real performance. Alternate endpoints for the same document are not independent corroboration.

| Finding | Correction |
|---|---|
| The supposed legacy Tesla snapshot was a mutable live URL | Retired S05 from active claims; checked the original 2017 Tesla transcript and replaced historical citations |
| The first edition relied on secondary summaries for details now available directly | Rechecked original Tesla, Hagerty and Top Gear passages; recorded locations for every structured claim |
| A malformed voltage caption left an avoidable gap | Top Gear 6:12 explicitly describes an 800–1,000-volt range; still provisional, not a final nominal rating |
| Acceleration reports used different precision and conventions | Preserved the event’s announced 0.81 seconds, rollout-qualified interview figures and other attributed reporting separately |
| Charging descriptions were too easy to collapse into one specification | Preserved the ten-minute goal, under-fifteen-minute narration and an ambiguous caption; no final charge curve inferred |
| Two newer patents were represented only by index metadata | Initial gazette/abstract checks were expanded to original PDFs and all claims; force figures and distinct embodiments are preserved. Prosecution and legal analysis remain outside scope |
| Article publication date could be mistaken for original teaser-post time | September 12 timeline entry now identifies the report date explicitly |
| HTTP failures could be mistaken for source inaccessibility | AP was reverified through the ordinary browser after HTTP and web-extraction failure; access method is recorded |
| The reservation agreement initially appeared unreadable | Recovered the rendered two-page US v.20261015 PDF, reviewed all ten clauses and rejected a stale search preview. Incorporated policies are now separately reviewed; later contracts and post-configuration refunds remain unresolved |

## Code defects corrected

- Malformed JSON rows, missing IDs and invalid field types could crash validation. They now produce actionable validation errors.
- A readable reporter could incorrectly satisfy the direct-primary-source gate. Direct manufacturer/interview claims now require an appropriate directly reviewed primary source.
- Blocked or obsolete citations could remain active evidence. Active claim references now reject those access states.
- Source, claim and timeline edits could silently inherit an earlier audit. Review hashes now detect changed records. These hashes detect changes; they do not prove a reviewer’s honesty or factual correctness.
- Finite inputs could overflow calculations and cause a JSON traceback. All calculator functions now reject non-finite results with an actionable error.
- The renderer split escaped table pipes, discarded README fragments, mishandled encoded paths and crashed on protocol-relative links. Those reproduced cases have regression tests.
- Every Mermaid block was replaced with one hard-coded diagram. The actual diagram source is now preserved, with the rendered GitHub version identified as the reading option.
- Edition dates and era choices were hard-coded. The footer, explorer date and era menu now follow data.
- A rebuild could retain obsolete generated chapters. A build manifest now removes only previously generated guide pages, preserves unrelated files, and checks generated file/anchor targets.

## Verification

The initial audit's **28 unit tests passed**; the later explorer fixes expanded the passing suite to **29 tests**. Data/review validation, generated Markdown freshness, generated HTML links/anchors, JavaScript syntax and patch whitespace checks are recorded in [the verification history](verification.md). The document and payment-policy follow-ups bring the original 19-page site to 21 pages.

Run the offline checks:

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/build.py
python3 tools/build.py --check
node --check site/app.js
```

The optional `tools/check_sources.py` probe records HTTP status, resolved URLs, response identity and timestamps. Access failures can be resolved separately through browser or web text inspection. HTTP success alone is not source verification. The actual access observations are saved in this research directory; full articles, transcripts and patent files are not redistributed.

## Remaining limits

The current US agreement's ten clauses and incorporated payment/privacy policies within the stated scope are reviewed. Later contracts, accepted policy versions, post-configuration refund amounts, modification meaning and enforceability remain open. All three patent claim sets are read, but production implementation and prosecution/legal analysis remain unverified. AP was recovered through normal browser reading. The retired legacy snapshot has no recovered immutable copy, and the two newer patent indexes remain metadata evidence. Relevant video captions and descriptions were inspected, not every frame and audio passage. The ambiguous charge-window caption still needs audio reconciliation. See [the document follow-up](document-review.md) for precise scope and receipts.

No independent instrumented production-car test, final price list, certified range, final battery capacity, regulatory clearance or customer-delivery evidence was established. These are explicitly scoped research gaps, not conclusions that such evidence cannot exist. See [open questions](../docs/open-questions.md).
