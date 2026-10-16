# Reservation and patent document review

[Home](../README.md) · [Availability](../docs/availability.md) · [Engineering](../docs/engineering.md) · [Review ledger](../docs/audit-ledger.md)

Checked **October 16, 2026**. This follow-up resolves the earlier reservation-PDF access gap and expands the patent review beyond index metadata and an abstract. It describes written documents; it does not establish enforceability, production fitment or measured vehicle performance.

## The current US reservation agreement

The US configurator links to [S41, Tesla's current agreement](https://www.tesla.com/coinorder/api/v4/terms?locale=en_US&model=mt&saleType=PreSale). Its two-page footer identifies **US v.20261015**. Both pages and all ten numbered clauses were extracted and visually checked. [S49, an alternate official endpoint](https://www.tesla.com/configurator/api/v4/terms?locale=en_US&model=mt&saleType=PreSale), exposes the same version and material clauses. These are two routes to the same agreement, not independent contractual evidence.

| Location | What the written document says |
|---|---|
| Page 1, clause 1 | Effectiveness requires the reservation and full payment, including the installment due within ten days. |
| Page 1, clauses 2–3 | An estimate is provisional. Reservation precedes configuration, ordering and final purchase contracts; payment is credited if the purchase proceeds. |
| Page 1, clause 4 | Neither delivery timing nor eventual delivery is guaranteed. |
| Page 1, clause 5 | Either party may cancel through the Tesla Account with a full reservation-payment refund until the customer completes configuration following Tesla's invitation. Refund routing uses the original payment method, with a named-holder check fallback. |
| Page 1, clause 6 | Funds are not segregated into escrow/trust, earn no interest, and transfer needs Tesla's prior written consent. |
| Page 1, clause 7 | Other privacy and payment policies are incorporated. |
| Page 1, clauses 8–9 | The text limits remedies and damages and sets an address-related governing-law rule and integration provision. |
| Page 2, clause 10 | It specifies a notice/dispute process, individual AAA arbitration, fee allocations, restrictions on collective proceedings, a small-claims alternative and a written opt-out within 30 days after signing. Read the full clause for its conditions. |

The cancellation cutoff is **completion of configuration**, not a cutoff silently taken from an older search preview. Clause 4 also addresses **whether** delivery occurs, not just its date. The document's version identifier is recorded; its original publication time is not independently established.

The configurator separately says refunds for modifications will not be issued. The reservation PDF does not fully explain that phrase or establish post-configuration rights. The [incorporated payment/privacy policies have since been reviewed within a stated scope](payment-policy-review.md). They do not resolve post-configuration refund amounts. Future Order/Purchase Agreements, other countries and enforceability in a particular case remain open. No agreement was accepted and no reservation or payment was made.

## Read the three patent disclosures separately

An independent claim states a combination on its own. A dependent claim adds requirements by referring back to another claim. The descriptions contain additional examples; a number appearing there is not automatically a requirement of every claim.

| Document | Original reviewed | Claim map and useful distinction |
|---|---|---|
| [S50: US12377920B1](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12377920), adaptive downforce | 16 PDF pages; 20 claims, on PDF pages 15–16 / printed columns 18–20 | Independent claims 1 and 11 concern fan airflow and changing skirt configurations between two modes. Dependent claims address partial deployment, multiple bounded regions, sensors and ground proximity. The cover identifies Tesla and an August 5, 2025 grant. |
| [S48: US12746987B1](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12746987), electric fan car | 9 PDF pages; all 15 claims on PDF page 9 / printed columns 5–6 | Independent claims 1, 7 and 10 include an underbody inlet, rear outlet with larger cross-section, and outlet strakes—vanes between adjacent fans. Claim 10 additionally specifies axial fans, traction-battery power and side inlets. The cover identifies Tesla and a September 29, 2026 grant. |
| [S47: US20260285418A1](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/20260285418), rear wing | 29 PDF pages; paragraphs 0001–0147; all 20 claims on PDF pages 28–29 / printed pages 12–13 | Independent claims 1, 14 and 20 describe different combinations of wing elements, deployment, rotation, control and impact protection. This is an application publication dated September 24, 2026, rather than a reviewed grant. |

### Fan count and skirts are embodiment choices

The fan-car grant's description (printed columns 2–4) discusses four fans and other counts, and an example that can operate without a road-contact skirt. Its claims do not establish a mandatory four-fan, 20-kW-per-fan Roadster specification. The adaptive-downforce grant instead expressly claims selectable skirt configurations. These are distinct disclosures; they do not establish which combination a production Roadster will use. Interview specifications remain separate evidence.

### The wing's force figures need their locations attached

Paragraph **0046** (PDF page 20 / printed page 4) describes an example with zero downforce in DRS mode and **up to 700 kg** in high-downforce mode at top speed, giving speeds above 100 mph as an example. Dependent **claim 10** (PDF page 29 / printed page 13) instead recites **400–500 kg** when deployed. These passages have different contexts and cannot be collapsed into a single verified Roadster specification.

The document uses kilograms as downforce shorthand. That should not be read as vehicle mass or as an independently measured force. No complete force-versus-speed curve is supplied by those passages.

Paragraphs **0024, 0065 and 0070** describe deployment below three seconds and rotation below a quarter-second in examples. Claims **8–9** specify a 3–15 mm slat position and deployment below three seconds; claims **11–13, 16–17 and 19** address impact-retraction arrangements. These are technical disclosures, not this project's verification of actuator speed, pedestrian protection or regulatory compliance. Paragraph **0104** describes CFD/wind-tunnel work but is not an independently reviewed test dataset.

## Access and identity receipts

Direct HTTP access to the current agreement still returned 403. Its native browser PDF rendered despite an empty accessible-text tree; the already-loaded document bytes were recovered, extracted and rendered locally. The alternate Tesla endpoint also provided readable official PDF extraction. A stale search preview was not substituted for the opened PDF.

The patent PDFs were retrieved from USPTO. Their text layers were empty, so OCR was used to navigate the documents. All claim sets were read; the claim pages and numeric passages used above were checked against rendered originals. Relevant adaptive-downforce description passages were reviewed; this was not an exhaustive legal analysis of every example or drawing detail.

[Document identity receipts](document-access-2026-10-16.json) record byte counts, PDF page counts, SHA-256 hashes and review scope. Complete PDFs, OCR dumps, browser state and the agreement text are not republished here. Hashes identify retrieved bytes; they do not establish authenticity or legal validity.

## Gaps that remain

- Later applicable Roadster contracts, accepted policy versions and the post-configuration/refund-modification interaction; see the [payment-policy follow-up](payment-policy-review.md).
- Patent prosecution, amendments, family/legal-status research, validity and freedom to operate; which embodiments actually ship.
- Independent performance data, final battery capacity, charge curve and certified range.
- Audio reconciliation of the ambiguous charging caption and a final explanation of air replenishment versus nitrogen refill.

The document-access gaps improved. The vehicle's physical capabilities and final customer terms still require additional evidence.
