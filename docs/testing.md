# Understand performance measurements

[Beginner’s guide](start-here.md) · [Compare versions](2026-reveal.md) · [Claims and sources](claims.md)

A smaller acceleration time does not always mean a faster car: the finish speed, clock settings and test conditions may differ. Start with those details before comparing headlines. The worked examples below are **invented teaching examples, not measured Roadster results**.

## 1. Check the finish speed

**0–60 mph** describes accelerating from rest to 60 miles per hour. **0–100 km/h** ends at 100 kilometres per hour, a higher speed: 60 mph is about **96.6 km/h** (exactly 96.56064). The next section explains why some quoted times leave out part of the start.

For example, two cars taking 2 seconds to reach these different speeds have not performed the same test. Converting the speed units does not tell you the extra time needed to reach 100 km/h. [NIST’s unit-conversion reference](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9)

## 2. Check when the clock starts

**Rollout** means leaving out a short initial distance from the timed portion of an acceleration run. With one-foot rollout, the clock leaves out the time spent travelling the first foot, about 30 centimetres. The car is already moving when the counted interval begins.

**Invented example: the same run, two reported times.**

1. The car takes **2.00 seconds** from actual rest to the finish speed.
2. In this example, travelling the first foot takes **0.30 seconds**.
3. Excluding that start gives **2.00 − 0.30 = 1.70 seconds**.

The car did not become faster; the reported time excludes part of its motion. The excluded time varies with the run. **Do not add 0.30 seconds to every rollout figure**—that number belongs only to this example.

## 3. Understand average, peak and “g”

**Acceleration** describes how quickly speed changes. **Average acceleration** covers the whole measured interval. **Peak acceleration** is the highest value reached during it; it does not tell you how long that value lasted.

**g** expresses acceleration relative to standard gravity. One g is about 9.81 metres per second squared: a speed change of about 9.81 metres per second, each second. It is a unit of acceleration, not speed. The exact reference is 9.80665 m/s². [NIST’s standard-gravity reference](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9)

**Optional worked example: 60 mph in 0.85 seconds from actual rest.**

1. Convert the finish speed: 60 mph = **26.8224 metres per second**.
2. Divide the speed gained by the full time: 26.8224 ÷ 0.85 ≈ **31.56 m/s²**.
3. Express that in g: 31.56 ÷ 9.80665 ≈ **3.22 g average acceleration**.

That does not mean the car accelerates at 3.22 g throughout the run. Try the [online calculator](https://fhajjej-ship-it.github.io/roadster-reference/#lab) without installing anything. It assumes the entered time covers the entire run from rest; it cannot recover the missing start from a rollout time. It also does not model how abruptly acceleration changes or the forces on a person, so it cannot establish safety or verify a claimed vehicle result.

## Apply those checks to Roadster reports

The reviewed sources report several numbers:

- The [Hagerty interview, 16:28 onward](https://www.youtube.com/watch?v=22rvpUecLts&t=988s) qualifies **0.55 seconds** as using rollout and distinguishes Performance, Thrust and Rocket.
- The [official reveal, 18:30](https://www.youtube.com/watch?v=qt5p-_tE8d0&t=1110s) announces **0.81 seconds**.
- [Car and Driver](https://www.caranddriver.com/news/a74145531/tesla-roadster-revealed/) reports **0.8 seconds**, to one decimal place; [Top Gear](https://www.topgear.com/car-news/electric/tesla-roadster-has-finally-landed-thrusters-0-60mph-059s-and-flight) uses **0.59 seconds**.

These may differ in test method, vehicle equipment, rounding, individual run or intended target. The reviewed evidence does not resolve every difference. The numbers alone establish neither a contradiction nor a verified fastest-car record.

## What to look for in a test report

- **Which car?** Its version, equipment, software, weight and whether it is a development prototype or a customer production car.
- **How was it timed?** The measuring device, what started the clock, any rollout, the finish speed and the original speed-versus-time recording, sometimes called a **raw trace**.
- **What conditions?** Road slope, surface treatment to improve grip, weather, wind and temperature; tire type, pressure, wear and temperature.
- **What starting state?** Battery charge and temperature, plus the gas supply before and after using thrusters.
- **Can it repeat the result?** Several runs, the variation between them and any cooling or gas refilling needed between attempts.
- **Who checked it?** Who controlled the setup, recorded the data and reviewed the result. A demonstration or company announcement is different evidence from an independently measured test.

This is a checklist for evaluating evidence, not a statement that these Roadster tests have been completed.

## Driving range: ask which test was used

**Range** means distance on a charge. A **test cycle** is a specified driving schedule, including changes in speed, used to make tests repeatable.

- **EPA** is the US Environmental Protection Agency. EPA range uses laboratory tests and adjustments intended to reflect real-world driving. It is not simply battery energy divided by an assumed energy use per mile. [EPA’s explanation](https://www.epa.gov/greenvehicles/fuel-economy-and-ev-range-testing)
- **WLTP** means Worldwide harmonised Light-duty vehicles Test Procedure, another standardized test procedure used in Europe. Its results should not be treated as interchangeable with EPA ratings. [EU’s WLTP overview](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=LEGISSUM%3A4390810)

A steady-speed drive and a manufacturer’s target are different again. Ask which procedure produced the number. This research has not established an applicable EPA rating for the new Roadster; a press report saying “300-plus miles” does not establish range with fans or thrusters running continuously.

## Compare like with like

Rimac’s [Nevera R page](https://www.rimac-automobili.com/NeveraR/) lists different 0–60 mph and 0–100 km/h times. McMurtry’s [fan-car demonstration](https://mcmurtry.com/upside-down-driving/) illustrates a relevant mechanism. Neither supplies a comparison with the redesigned Roadster tested under matching conditions. Sorting unmatched figures cannot establish a fastest-car title.

**Finished the introductory path?** [Choose another topic in the beginner’s guide](start-here.md#where-to-go-next), or [check an individual claim and its sources](claims.md).
