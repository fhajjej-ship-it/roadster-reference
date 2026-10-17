# Roadster Reference

**An independent, open-source field guide to the new Tesla Roadster.**

Understand how the car works, follow claims to their original sources, and see what remains unknown. This community learning resource separates Tesla's claims, reported observations and research gaps so you can assess the evidence for yourself.

**New here? [Read the beginner’s guide](docs/start-here.md)** for the basic mechanisms, vocabulary and a suggested reading path. No engineering background is needed to begin.

**[Open the website](https://fhajjej-ship-it.github.io/roadster-reference/)** to browse the same research with search and calculators — no installation or account required.

- **How does it work?** Learn about the motors, battery, fan suction, active wings and cold-gas thrusters in the [engineering guide](docs/engineering.md).
- **What do the performance numbers mean?** Understand rollout, test conditions and fair comparisons in the [measurement guide](docs/testing.md).
- **Where is the evidence?** Trace statements through the [claim ledger](docs/claims.md) and [annotated sources](docs/sources.md).
- **What still needs an answer?** Explore unresolved specifications, testing, delivery and customer terms in the [open questions](docs/open-questions.md).

<p align="center"><img src="https://digitalassets.tesla.com/tesla-contents/image/upload/f_auto,q_auto/Roadster-03-Carousel-Slide-1-Desktop.jpg" alt="Front view of the white 2026 Tesla Roadster — official Tesla product imagery" width="100%"></p>

<p align="center">2026 Roadster · <a href="https://www.tesla.com/roadster">Image: Tesla</a> · External image; rights retained by Tesla.</p>

**Research cutoff: October 16, 2026.** A curated first edition, not a live feed or an exhaustive archive. Tesla has demonstrated a redesigned prototype; the reported production target is **2028**, not a verified delivery date. [Reuters](https://live.euronext.com/en/financial-news/teslas-new-roadster-turns-air-spacex-thrusters-wont-land-until-2028)

> **Read this first:** the 2017 red concept and the October 2026 redesign are different evidence sets. Do not combine the old 620-mile / four-seat claims with the new car’s specifications. [Original Tesla reveal, 31:10](https://www.youtube.com/watch?v=5RRmepp7i5g&t=1870s) · [Current Tesla page](https://www.tesla.com/roadster)

## Choose a topic

After the beginner’s guide, follow any topic that interests you. These are optional routes, not steps you must complete in order.

| You want to… | Go here |
|---|---|
| Get the basics first | [Beginner’s guide](docs/start-here.md) |
| Compare Performance, Thrust and Rocket | [2026 reveal and configuration guide](docs/2026-reveal.md) |
| Learn how fans, wings and thrusters work | [Engineering explained](docs/engineering.md) |
| Make sense of spectacular acceleration numbers | [Measurement guide](docs/testing.md) |
| Reproduce the math | [Physics lab](docs/physics-lab.md) |
| Trace deadlines and recent news | [Dated timeline](docs/timeline.md) |
| Find original material and assess its limits | [Annotated source library](docs/sources.md) |
| Identify what still needs evidence | [Open questions](docs/open-questions.md) |
| Understand road-use and reservation context | [Availability and regulation](docs/availability.md) |
| Understand refunds and the configuration cutoff | [Payment-policy review](research/payment-policy-review.md) |
| Contribute a correction | [Contribution guide](CONTRIBUTING.md) |

## What has been reviewed

The audit and follow-ups cover **52 source records, 42 structured claims and 15 timeline events**. **49 sources support their stated scope, 2 patent indexes retain limited verification, and 1 obsolete citation is retired.** The current US reservation PDF, incorporated payment/privacy policies within the stated scope, and all three patent claim sets are reviewed. Later contracts, post-configuration refund amounts, prosecution and production fitment remain open. See the [payment and refund findings](research/payment-policy-review.md), [document findings](research/document-review.md), [audit](research/audit.md) and [record-by-record review](docs/audit-ledger.md). Source counts include alternate endpoints for the same documents and do not count independent corroboration.

## What makes this useful

- Every structured claim has source IDs, a vehicle era, a status, a checked date and an unresolved question.
- Manufacturer claims, reported observations, historical targets and unknowns stay distinct.
- A searchable, responsive browser explorer works locally without a backend or third-party libraries.
- Reproducible calculators explain acceleration, drag, suction force and energy using explicit inputs.
- The research log records inaccessible material and review limits.
- Audit receipts are bound to the exact records, so an edited claim cannot silently retain an old review.

The aspiration is to become a dependable reference. Popularity, completeness and technical superiority are not established by publishing a repository.

## Explore locally

The [public explorer](https://fhajjej-ship-it.github.io/roadster-reference/) publishes automatically from `main` after the repository checks pass. The [Pages workflow](.github/workflows/pages.yml) builds and deploys only `site/dist/`; generated files stay out of Git.

Requires Python 3.11+; no packages, API keys or account required.

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/build.py
python3 -m http.server 8765 --directory site/dist --bind 127.0.0.1
```

Open [the local explorer](http://127.0.0.1:8765). It includes claim/source search, era and evidence filters, the timeline, learning chapters and an acceleration calculator. The generated HTML also opens directly from disk. GitHub itself renders the complete Markdown guide.

```sh
python3 tools/physics.py acceleration --time 0.85 --mass 1800 --speed-mph 60
python3 tools/physics.py drag --speed-mph 230 --cda 0.60
python3 tools/physics.py suction --pressure-pa 5000 --area-m2 3
python3 tools/physics.py range --usable-kwh 100 --wh-per-km 200
```

These are educational scenarios, **not measured Roadster specifications or vehicle-control software**. The example mass, drag area, pressure, area and battery capacity are hypothetical.

## Repository map

```text
data/       Source registry, claim ledger, timeline and edition metadata
docs/       Learning chapters and generated reference tables
research/   Method, access notes, interview locators and coverage gaps
tools/      Standard-library build, validation and physics code
site/       Accessible, static reading interface
tests/      Numerical and evidence-integrity checks
assets/     Original repository artwork
```

## Independence and reuse

This is a community educational project, unaffiliated with Tesla or SpaceX. It contains original explanations and software, links to public material, and attributed factual summaries. It contains no Tesla firmware, leaked files, service credentials or proprietary vehicle code. External articles, videos, trademarks and patent rights remain with their owners.

Original code and project-authored content are available under the [MIT License](LICENSE), subject to [third-party rights](THIRD_PARTY_NOTICES.md). See [how to cite this project](CITATION.cff), [editorial method](research/methodology.md) and [contributing](CONTRIBUTING.md).
