# First-edition verification

Performed October 16, 2026, before initial publication.

- Nine Python unit tests passed: exact speed conversion; a known acceleration/energy example; mass scaling; drag power scaling; pressure-area dimensions; energy/consumption range; invalid/non-finite denominators; zero-motion limits; and evidence integrity.
- The data validator resolved all claim/timeline source references, checked dates and statuses, retained legacy-era labels, and checked local Markdown links.
- The static generator completed. Generated Markdown freshness was checked with `python3 tools/build.py --check`.
- JavaScript syntax passed `node --check site/app.js`.
- Generated HTML local links and fragment targets were checked without external requests.
- A real browser loaded the explorer and engineering chapter. Search for `nitrogen` returned the relevant claims and one source record. Source/claim totals were present.
- The browser calculator at 0.85 s / 1,800 kg / 60 mph displayed 3.22 g, 56.8 kN, 0.180 kWh and 11.40 m. Changing time to 2 s displayed 1.37 g, 24.1 kN, 0.180 kWh and 26.82 m, consistent with the Python model.
- Desktop layout was visually inspected; an image-cropping issue was corrected. Responsive CSS is provided; a separate mobile-device test was not performed.

A mistaken expected energy constant in the first test run was corrected against the independently calculated value, 0.0999223808 kWh for 1,000 kg at 60 mph. The published test suite passes. A documentation drag-power approximation was also corrected to match the executable result.

These checks validate the original repository software and evidence structure. They do not independently validate Tesla’s vehicle, manufacturer performance claims, legal status, safety or production plans. Source-access limits are recorded separately in the research method and registry.

## Audit verification — October 16, 2026

The subsequent [repository audit](audit.md) expanded the suite to **28 passing tests**. The added regressions cover malformed/missing data, false primary-source attribution, blocked citations, stale review hashes, floating-point overflow, escaped table pipes, README fragments, encoded/protocol-relative links, diagram-source preservation, data-derived dates/era choices, generated anchors and obsolete generated-page cleanup with unrelated-file preservation.

Validation passed for all 47 source records, 33 claims and 15 timeline events, including bound review records and local Markdown links. The generator built 19 HTML pages and checked their local files and fragments. Generated Markdown freshness, JavaScript syntax and `git diff --check` passed. These are software/evidence-structure checks; source review outcomes and remaining access limitations are recorded separately in the audit ledger.

A fresh browser load showed 33 claims and 47 sources. Searching `1585` isolated C17 and exposed both interview links and timestamps. Choosing the data-derived `2017` era showed five historical claims. At 2 s / 1,800 kg / 60 mph the calculator returned 1.37 g, 24.1 kN, 0.180 kWh and 26.82 m. The rendered audit report was read and visually inspected. A mobile-device test was not performed.

## Explorer desktop and mobile audit — October 16, 2026

The published Pages explorer was inspected at desktop and phone viewport sizes. An anonymous HTTP check covered all 19 published HTML pages, 22 unique internal page/asset targets and their local fragments; no broken internal target or fragment was found. External publishers' blocked/retired evidence links retain their documented limitations; this was not another external-source revalidation.

Reproduced and fixed:

- A long inline commit hash made the audit article wider than a 320-pixel phone viewport. Article text and inline code now wrap; code blocks and wide tables retain their own horizontal scrolling.
- Phone calculator fields used 12-pixel text in cramped three-column rows. They now use 16-pixel input text and stack at narrow widths; mobile navigation and claim disclosures have 44-pixel minimum targets.
- An invalid calculator submission could leave a previous valid result visible. Editing an input now clears the old result and requests recalculation.
- Empty or distant search results offered no direct reset or convenient route between controls and matching sources. Added reset/focus recovery, a source-result shortcut with its count, and a return-to-search link.
- Wide chapter tables lacked an explicit keyboard focus target and mobile scroll cue. They now have a named, focusable scroll region and a cue; right-arrow scrolling was exercised in the browser.
- Diagram instructions mentioned a rendered GitHub diagram without linking to it. The generated instruction now links to its original chapter.

After these fixes, all 19 generated pages were checked at **320, 390, 800 and 1,440 CSS pixels** (76 page/width combinations), with no document-level horizontal overflow. Browser checks covered empty search, combined filters, reset to 33 claims/47 sources with search focus restored, invalid-input result clearing, and the 2-second calculator scenario. All **29 unit tests**, data validation, generated Markdown freshness, generated HTML links/anchors, JavaScript syntax and whitespace checks passed.

These are browser viewport and keyboard checks, not a physical iPhone/Android, mobile software-keyboard or full screen-reader certification.

## Reservation and patent follow-up — October 16, 2026

The [document review](document-review.md) records recovery of the two-page US v.20261015 reservation PDF, review of all ten clauses, and an alternate official extraction with matching version/material clauses. Three original USPTO PDFs were retrieved, with 20, 15 and 20 claims respectively. Claim pages and the wing's force/timing passages were visually checked after OCR. [Identity receipts](document-access-2026-10-16.json) retain document hashes, page counts and exact review limits without redistributing full texts.

The registry now has 50 sources, 40 claims and 15 events with bound reviews. The suite still has **29 passing tests**. Its blocked-access regression now sets the access state in its fixture instead of assuming the real S41 agreement stays blocked forever. Data validation, a 20-page HTML build, local links/anchors, generated Markdown freshness, JavaScript syntax and whitespace checks passed. Earlier counts above describe their original verification runs.

## Incorporated payment-policy follow-up — October 16, 2026

The [payment-policy review](payment-policy-review.md) records the exact configurator-linked policy URLs, reviewed section boundaries, refundable/modification wording, unresolved later contracts and rejected substitutes. Two rendered-text identity receipts distinguish browser text from original HTTP bytes. New S51–S52 and C41–C42 have bound review records; changed S02, S41 and C34 reviews were updated only for the verified scope.

All **29 tests** passed. Validation covers 52 sources, 42 claims and 15 events. The generator built 21 HTML pages and checked local targets/fragments; generated Markdown freshness, JavaScript syntax and whitespace checks passed. No runtime code or dependencies changed. Earlier counts above remain the results of their original runs.

## Roadster image mobile check — October 17, 2026

The live image retained the whole vehicle at 320 and 390 CSS pixels without page overflow. Two layout issues were reproduced: the 500-pixel-wide image sat off-center in the 700-pixel mobile layout, and the source-credit link was approximately 20 pixels high. The mobile figure now centers within its column and the credit has a 44-pixel minimum tap height, with a readable caption. The existing image crop is retained.

Browser checks of the corrected layout at 320, 390, 700 and 1,280 CSS pixels confirmed image loading and no page overflow; the mobile image was centered and the credit target measured 44 pixels within rendering tolerance. These are browser viewport checks, not physical-device certification.

## First-time visitor review — October 17, 2026

The rendered GitHub README, homepage topic choices and configuration destination were reviewed in a browser. The README now offers the beginner guide and website before its image, and places detailed review counts after the topic routes. Homepage topics are explicitly optional; the configuration card now opens the actual comparison rather than the beginner overview. Timeline, refund and physics shortcuts and a link explaining evidence labels make the remaining routes discoverable.

The beginner guide, all four topic cards, refund page, evidence-label section, timeline and calculator jumps were followed in the browser. The topic section was checked at 320 and 1,280 CSS pixels without page overflow. This is an editorial/navigation review, not a study with first-time users or a complete assistive-technology audit.
