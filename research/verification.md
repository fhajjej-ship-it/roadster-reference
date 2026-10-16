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
