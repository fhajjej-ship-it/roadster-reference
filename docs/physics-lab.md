# Reproduce the physics

[Home](../README.md) · [Engineering](engineering.md) · [Measurement caveats](testing.md)

All inputs below are **hypothetical**. They are not a hidden Roadster specification sheet. Standard gravity is 9.80665 m/s²; the exact mph-to-m/s conversion is 0.44704.

## Acceleration

```sh
python3 tools/physics.py acceleration --time 0.85 --mass 1800 --speed-mph 60
```

This treats the chosen time as the entire interval from actual rest. It gives approximately 3.22 g average acceleration, 56.8 kN average net force, and 0.180 kWh of translational kinetic energy. Distance assumes constant acceleration. The energy is an ideal kinetic quantity; electrical energy drawn would also include losses, rotating parts and any other consumers. If you enter a rollout-subtracted time, the output does not reconstruct the missing beginning of the run.

## Aerodynamic drag

```sh
python3 tools/physics.py drag --speed-mph 230 --cda 0.60
```

This uses hypothetical drag area of 0.60 m² and default air density of 1.225 kg/m³. It yields approximately 399.5 kW of aerodynamic power. It excludes rolling resistance, grade, drivetrain losses, fans and accessories. Keeping drag area fixed, twice the speed requires eight times the aerodynamic power. [NASA drag model](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/)

## Suction

```sh
python3 tools/physics.py suction --pressure-pa 5000 --area-m2 3
```

The ideal force is 15 kN, equivalent to approximately 1,530 kg under standard gravity. This is not a mass added to the car. The model omits leakage, nonuniform pressure, power requirements and operating margin. It is insufficient to design or certify an inverted vehicle.

## Energy and range

```sh
python3 tools/physics.py range --usable-kwh 100 --wh-per-km 200
```

The arithmetic gives 500 km, approximately 311 miles, for those inputs. It does not establish what battery capacity the new Roadster has. Consumption varies with speed, temperature, tires, weather, accessories, fans and driving cycle. See [EPA testing context](https://www.epa.gov/greenvehicles/fuel-economy-and-ev-range-testing).

## What the software does

The command line prints the inputs, model description and explicit output units as JSON. Non-finite, negative and physically invalid denominator inputs are rejected. The browser lab implements the same acceleration equations and is checked against Python outputs during development. There is no vehicle connection, telemetry feed, firmware, simulation of flight control or external API.

Run meaningful numerical checks with:

```sh
python3 -m unittest discover -s tests -v
```
