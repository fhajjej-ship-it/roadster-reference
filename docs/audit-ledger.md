# Record-by-record audit

[Home](../README.md) · [Findings and limits](../research/audit.md)

Reviewed 2026-10-16. A supported attribution is not independent validation of a car.

## Sources

| ID | Outcome | Method and locator | Finding |
|---|---|---|---|
| [S01](https://www.tesla.com/roadster) | supported | browser: Configurations, aerodynamic explanation, steering and page footnotes | Direct product-page text matches the scoped manufacturer claims; no independent performance proof implied. |
| [S02](https://www.tesla.com/roadster/reserve) | supported | browser: US Performance and Thrust payment tables; Rocket selector | Both payment schedules and the invite-only selector were rechecked. No payment was made or agreement accepted. |
| [S03](https://www.youtube.com/watch?v=qt5p-_tE8d0) | supported | browser-transcript: 4:39; 12:21–12:36; 18:30; 20:28; 21:12 | Relevant original event captions support autonomy, replenishment description, announced timing and stated targets. |
| [S04](https://www.youtube.com/watch?v=5RRmepp7i5g) | supported | browser-transcript: 29:39–33:27 | Original manufacturer transcript now directly supports the legacy specifications and 2020 availability target. |
| [S05](https://www.tesla.com/roadster?lang=en) | superseded | HTTP and browser comparison: URL now presents the redesigned product | No durable legacy snapshot recovered. Retired from active claims; historical evidence moved to S04. |
| [S06](https://live.euronext.com/en/financial-news/teslas-new-roadster-turns-air-spacex-thrusters-wont-land-until-2028) | supported | HTTP full text: Reuters byline, McGregor event and final specification paragraphs | Article identity, update date and attributed production/range/speed claims checked; not an instrumented test. |
| [S07](https://apnews.com/article/tesla-musk-roadster-rocket-7d5f19665435b7408025bfb7a2f2f0b7) | supported | browser: Event account, 2028 target, reservation caveat and autonomous-demo paragraphs | HTTP and web extraction failed, but direct browser reading resolved access. Expert opinions remain distinct from regulatory findings. |
| [S08](https://www.caranddriver.com/news/a74145531/tesla-roadster-revealed/) | supported | HTTP full text: Second acceleration run and separate-stunt-prototype paragraphs | Article reports 0.8-second rounding and distinguishes the stunt prototype; no timing protocol verified. |
| [S09](https://www.topgear.com/car-news/first-look/wow-new-tesla-roadster-can-actually-fly) | supported | HTTP full text: Opening eyewitness account and unmanned-car paragraph | Supports an attributed eyewitness account. Its delivery wording is not substituted for Tesla’s production target. |
| [S10](https://www.topgear.com/car-news/electric/tesla-roadster-has-finally-landed-thrusters-0-60mph-059s-and-flight) | supported | HTTP full text: Range, rear drive, charging and mass paragraphs | Interview-derived article claims verified as reporting; author summaries remain separate from executive quotes. |
| [S11](https://teslanorth.com/2026/10/16/tesla-roadster-moravy-hagerty-engineering-interview/) | supported | HTTP full text: Battery, powertrain, fan, tank and refill paragraphs | Summary is readable. Primary S12/S13 replace reliance on this summary where direct passages are now available. |
| [S12](https://www.youtube.com/watch?v=22rvpUecLts) | supported | browser-transcript: 2:41–7:50; 12:47–17:57; 18:43–20:25 | Relevant primary passages and publisher description rechecked; distinguish executive speech from presenter narration. |
| [S13](https://www.youtube.com/watch?v=JdkIOhFmbKI) | supported | browser-transcript: 6:12; 13:27–14:16; 16:49–17:08; 22:28 | Relevant original passages clarify voltage range, range claim, charging-caption ambiguity and nitrogen filling. |
| [S14](https://electrek.co/2026/09/12/tesla-roadster-october-1-reveal-teaser/) | supported | HTTP full text: September 12 byline and teaser paragraphs | Publication date is verified. Prose calls the original post Friday; timeline no longer assumes article date equals post date. |
| [S15](https://electrek.co/2026/09/28/tesla-roadster-demo-delayed-october-15-weather/) | supported | HTTP full text: September 28 byline and attributed rescheduling post | Supports Tesla’s attributed weather explanation; does not independently prove weather caused the delay. |
| [S16](https://techcrunch.com/2025/11/06/tesla-delays-reveal-of-production-roadster-2-to-april-fools-day/) | supported | HTTP full text: November 6, 2025 byline and April 1 target | Historical reveal target verified, not an event-completion claim. |
| [S17](https://uk.marketscreener.com/quote/stock/TESLA-INC-6344549/news/Tesla-aims-to-ship-Roadster-cars-next-year-Musk-says-46045322/) | supported | web full text: February 28, 2024 Reuters report, paragraphs 1–3 | Attribution and next-year target verified through web extraction after direct HTTP denial. |
| [S18](https://arstechnica.com/cars/2017/11/not-just-a-semi-announcement-tesla-promises-a-new-roadster/) | supported | HTTP full text: 2017 specification and pricing paragraphs | Historical proposal checked; original S04 now supports the technical claims directly. |
| [S19](https://fortune.com/2018/06/10/musk-tesla-roadster-spacex-rocket-thrusters/) | supported | HTTP full text: June 9 embedded post and COPV explanation | Confirms the historical proposal and announcement date; not delivered capability. |
| [S20](https://patents.google.com/patent/US12377920B1/en) | supported | HTTP full text: Bibliographic data and Abstract | Title, Tesla assignment listing, publication date and adaptive downforce description match. No fitment inferred. |
| [S21](https://eureka.patsnap.com/patent/US12746987B1) | limited | HTTP index text: Title, assignee and publication metadata | Index metadata confirmed. Official gazette S46 now independently verifies the grant identity and first claim. |
| [S22](https://eureka.patsnap.com/patent/US20260285418A1) | limited | HTTP index text: Title, applicant and publication metadata | Index metadata confirmed. Official application S47 verifies identity and abstract; index AI summaries are not adopted. |
| [S23](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/rocket-thrust-equation/) | supported | HTTP full text: Thrust Equation | NASA equation includes both momentum and nozzle-pressure terms; repository uses it as general physics. |
| [S24](https://www.nasa.gov/smallsat-institute/sst-soa/in-space_propulsion/) | supported | HTTP full text: Cold Gas technology description | No-combustion definition checked; spacecraft examples do not establish automotive performance or safety. |
| [S25](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) | supported | HTTP full text: Drag Coefficient and equation | Density, speed squared and reference area match the educational model; power is the project’s force-times-speed derivation. |
| [S26](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/dynamic-pressure/) | supported | HTTP full text: Dynamic Pressure equation | General dynamic-pressure context verified, not Roadster measurements. |
| [S27](https://afdc.energy.gov/vehicles/how-do-all-electric-cars-work) | supported | HTTP full text: Key Components of an All-Electric Car | Battery, motor, controller, thermal system and charging roles checked; vehicle-specific design not inferred. |
| [S28](https://www.epa.gov/greenvehicles/fuel-economy-and-ev-range-testing) | supported | HTTP full text: Range Testing for Electric Vehicles | Laboratory and adjustment context checked; no new Roadster rating found or claimed. |
| [S29](https://www.nhtsa.gov/importing-vehicle/importation-and-certification-faqs) | supported | web full text: Importing a conforming vs. a non-conforming vehicle | Manufacturer certification-label framework checked through official web text after HTTP denial. |
| [S30](https://www.nhtsa.gov/vehicle-manufacturers) | supported | web full text: vPIC and manufacturer portal sections | Portal descriptions verified; directory presence is not a Roadster approval record. |
| [S31](https://www.faa.gov/air-taxis) | supported | HTTP full text: Advanced Air Mobility overview | Background scope verified. Page title updated; no Roadster aircraft classification inferred. |
| [S32](https://mcmurtry.com/upside-down-driving/) | supported | HTTP full text: Stationary-inversion article and April 11 publication | Other manufacturer’s demonstration and date checked; no cross-car equivalence asserted. |
| [S33](https://www.rimac-automobili.com/NeveraR/) | supported | HTTP full text: Performance specifications | Separate 0–60 mph and 0–100 km/h figures match; manufacturer figures remain labeled as such. |
| [S34](https://www.rimac-newsroom.com/press-releases/rimac-automobili/rimac-nevera-r-becomes-new-0-400-0-champion-and-sets-24-performance-records) | supported | HTTP full text: July 9, 2025 heading and acceleration paragraph | Release date and manufacturer record announcement checked; no independent Roadster comparison. |
| [S35](https://service.tesla.com/docs/Public/Roadster/) | supported | HTTP full text: Roadster Service Information / Owner Manuals | Legacy 2008/2.0/2.5 manual list confirms historical scope. |
| [S36](https://ir.tesla.com/press-release/tesla-unveils-roadster-25-newest-stores-europe-and-north-america) | supported | web full text: July 1, 2010 release, opening paragraphs | Official historical revision identity and date checked after direct HTTP denial. |
| [S37](https://ir.tesla.com/_flysystem/s3/sec/000119312512081990/d279413d10k.html) | supported | HTTP full text: 2011 Form 10-K / Roadster production-run paragraph | Filing explicitly states 2,500 vehicles and January 2012. Does not establish present readiness. |
| [S38](https://www.nhtsa.gov/vehicle-safety/tires) | supported | web full text: Traction and Temperature sections | Official tire guidance checked after HTTP denial; no extreme-speed approval implied. |
| [S39](https://www.tesla.com/learn/closing-loop-and-recovering-material-our-batteries) | supported | web full text: August 13, 2026 heading and recycling process | Company-level recycling statement verified; no model-specific lifecycle result inferred. |
| [S40](https://x.com/Tesla/status/2110788059008819215) | supported | HTTP public post text: Tesla / Roadster event livestream / October 15 | Previously blocked post text is now readable. It supports the announcement only, not technical specifications. |
| [S41](https://www.tesla.com/coinorder/api/v4/terms?locale=en_US&model=mt&saleType=PreSale) | unverified | HTTP and browser access attempts: Agreement URL linked from the live US configurator | HTTP denied; browser view exposed no readable agreement body. Refund and delivery clauses remain unverified. |
| [S42](https://electrek.co/2026/04/22/tesla-roadster-unveil-delayed-again-earnings-call/) | supported | HTTP full text: April 22 byline and Q1-call attribution | Article date and tentative further demo delay checked; this is an attributed forecast. |
| [S43](https://www.transportstyrelsen.se/en/road/Vehicles/type-approval/what-is-a-type-approval/) | supported | HTTP full text: Approval authority and whole-vehicle sections | General Swedish guidance checked. Its imprecise directive terminology is not adopted over the EU regulation. |
| [S44](https://eur-lex.europa.eu/eli/reg/2018/858/oj/eng) | supported | HTTP full text: Original act and current-consolidation notice | Original legal framework verified; page identifies August 2, 2026 consolidation. No Roadster-specific determination. |
| [S45](https://www.tesla.com/en_ph/legal/additional-resources) | supported | web full text: Patent Pledge / Legal Effect | Standstill and no-licence wording checked; repository licence grants no Tesla patent rights. |
| [S46](https://patentsgazette.uspto.gov/week39/OG/html/1550-5/US12746987-20260929.html) | supported | official gazette HTML: Bibliographic data and claim 1 | Official assignee, application and ducted-fan claim checked; resolves the former index-only grant identity gap. |
| [S47](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/20260285418) | limited | official PDF visual review: Cover page / bibliographic data, abstract and figure | Official scanned application cover reviewed visually. Complete claims and asserted downforce were not audited. |

## Claims

| Claim | Outcome | Checked location |
|---|---|---|
| C01 | supported-as-attributed | Tesla product page / Performance; US configurator / Performance |
| C02 | supported-as-attributed | Tesla product page / Thrust; US configurator / Thrust |
| C03 | supported-as-attributed | Tesla product page / Rocket; US configurator / disabled Rocket option |
| C04 | supported-as-attributed | Tesla product page / Rocket note |
| C05 | supported-as-attributed | Tesla product page / Thrust description |
| C06 | supported-as-attributed | Tesla product page / Beyond The Limits of Physics and footnotes |
| C07 | supported-as-attributed | Tesla product page / Supersonic and steer-by-wire description |
| C08 | supported-as-attributed | US configurator / Performance / Payment |
| C09 | supported-as-attributed | US configurator / Thrust / Payment |
| C10 | supported-as-attributed | Tesla Event 21:12 |
| C11 | supported-as-attributed | Hagerty 7:32–7:50 |
| C12 | supported-as-attributed | Tesla Event 20:28 |
| C13 | reported-observation | Top Gear eyewitness report / opening stunts and unmanned-vehicle paragraphs |
| C14 | unresolved-comparison | Tesla Event 18:30; Hagerty 16:28–17:20 |
| C15 | supported-as-attributed | Hagerty 2:41–3:13 |
| C16 | supported-as-attributed | Hagerty 3:27; Top Gear 6:12 |
| C17 | unresolved-comparison | Hagerty 7:32–7:50; Top Gear 13:50; Top Gear narration 17:08 |
| C18 | supported-as-attributed | Hagerty 4:14–4:31 |
| C19 | supported-as-attributed | Tesla 2017 reveal 30:56 |
| C20 | supported-as-attributed | Tesla 2017 reveal 31:10 |
| C21 | supported-as-attributed | Tesla 2017 reveal 29:39 |
| C22 | supported-as-attributed | Tesla 2017 reveal 32:25–32:54 |
| C23 | supported-as-attributed | Tesla 2017 reveal 30:47 |
| C24 | bounded-finding | US configurator; Tesla event specification/production discussion |
| C25 | bounded-finding | Hagerty 7:32; Top Gear 16:49 |
| C26 | bounded-finding | Reviewed event reporting and research search families; see research/research-log.md |
| C27 | document-disclosure | US12377920B1 / bibliographic data and Abstract |
| C28 | supported-as-attributed | Hagerty 15:31; 17:28–18:56 |
| C29 | supported-as-attributed | Hagerty 12:47–13:05 |
| C30 | unresolved-comparison | Tesla Event 12:21–12:36; Hagerty 20:17–20:25 |
| C31 | supported-as-attributed | Hagerty 3:51; 5:20–5:45 |
| C32 | supported-as-attributed | Hagerty 16:28–17:13 |
| C33 | supported-as-attributed | Hagerty 16:42 |

## Timeline

| Event | Outcome | Sources |
|---|---|---|
| 2010-07-01 / Original Roadster 2.5 revision | supported-as-scoped | S36 |
| 2012-01 / Original production run ends | supported-as-scoped | S37 |
| 2017-11-16 / Next-generation concept unveiled | supported-as-scoped | S04, S18 |
| 2018-06-09 / SpaceX-package proposal | supported-as-scoped | S19 |
| 2024-02-28 / Another delivery target | supported-as-scoped | S17 |
| 2025-08-05 / Adaptive-downforce patent publication | supported-as-scoped | S20 |
| 2025-11-06 / April 1 demo target announced | supported-as-scoped | S16 |
| 2026-04-22 / Demo timing shifts again | supported-as-scoped | S42 |
| 2026-09-12 / October 1 teaser reported | supported-as-scoped | S14 |
| 2026-09-24 / Rear-wing application published | supported-as-scoped | S47 |
| 2026-09-28 / Reveal moves to October 15 | supported-as-scoped | S15 |
| 2026-09-29 / Electric fan-car grant published | supported-as-scoped | S46 |
| 2026-10-15 / Redesigned Roadster demonstrated | supported-as-scoped | S06, S09 |
| 2026-10-16 / New configurator checked | supported-as-scoped | S02 |
| 2028 / Current production target | supported-as-scoped | S03 |
