# Try the physics lab

[Beginner’s guide](start-here.md) · [Engineering](engineering.md) · [Measurement guide](testing.md)

Use this lab to see what changes when you change one number. A **model** is a simplified calculation with stated assumptions; it is not a test of a real car. **Every input below is an invented example, not a confirmed Roadster specification.**

## Start in your browser: no installation needed

The [online calculator](https://fhajjej-ship-it.github.io/roadster-reference/#lab) covers **acceleration only**. The other three models below use optional Python commands.

1. Enter **0.85** for time in seconds, **1800** for vehicle mass in kilograms, and **60** for the target speed in miles per hour (mph). Mass describes how much matter is in the vehicle; it is kept fixed in this model.
2. Select **Calculate scenario**. You should see **3.22 g**, **56.8 kN**, **0.180 kWh** and **11.40 m**.
3. Change only the time to **2** seconds and calculate again. You should see **1.37 g**, **24.1 kN**, **0.180 kWh** and **26.82 m**.

Taking longer reduces the average acceleration and force. The final motion energy stays the same because the mass and finish speed did not change. The calculated distance increases because this model spreads the speed increase evenly over a longer time.

## Read the acceleration results

- **Average acceleration, in g:** how quickly speed increases over the full interval. One g is the standard-gravity reference, about 9.81 metres per second of speed gained each second. This is an average, not the highest acceleration reached.
- **Average net force, in kN:** the combined forward push after opposing forces are accounted for. A **newton (N)** is a unit of force; one **kilonewton (kN)** is 1,000 N. This is not motor torque or a measurement of tire grip.
- **Translational kinetic energy, in kWh:** energy associated with the vehicle moving from place to place. A **kilowatt-hour (kWh)** measures an amount of energy. The result is not the energy drawn from the battery: losses, spinning wheels and other equipment would also need energy.
- **Distance at constant acceleration, in m:** distance in metres, assuming speed increases at the same rate throughout the run. The model can calculate average acceleration without that assumption, but its distance result needs it.

The clock must cover the **entire interval from actual rest**. **Rollout** excludes a short initial distance from some published times. Entering such a shortened time cannot reconstruct the missing start; see the [measurement guide](testing.md). Changes in mass as gas leaves a thruster are also not modeled.

## Optional: run the examples on your computer

You can read the results below without running anything. To reproduce them, you need [Python 3.11 or newer](https://www.python.org/downloads/) and a downloaded copy of this repository. No extra Python packages or API keys are needed.

A **terminal** is an app for typed commands. Open one in the repository’s top folder—the folder containing `README.md` and `tools/`. On GitHub, **Code → Download ZIP**, followed by extracting the ZIP, is one way to get the files. Check that Python is available:

```sh
python3 --version
```

Then copy a whole command below and press Enter. If `python3` is not found, complete Python setup first. On Windows, your installation may use `py`; if so, replace `python3` with `py` at the start of each command. If Python cannot find `tools/physics.py`, check that the terminal is in the repository’s top folder.

In each command, a name beginning with `--` identifies a setting; the number after it supplies its value. The program prints **JSON**, a text format containing named values. Read `inputs` to confirm your settings and `results` for the answers. Underscores in names join words: `average_acceleration_g` means average acceleration expressed in g.

### 1. Acceleration: how quickly does speed change?

This is the same example as the browser exercise. `--time` is the full time from rest, `--mass` is kilograms, and `--speed-mph` is the finish speed.

```sh
python3 tools/physics.py acceleration --time 0.85 --mass 1800 --speed-mph 60
```

- `average_acceleration_g` ≈ **3.22**; `average_net_force_n` ≈ **56,800 N**, or 56.8 kN.
- `kinetic_energy_kwh` ≈ **0.180**; `constant_acceleration_distance_m` ≈ **11.40**.
- The extra Python output `average_kinetic_power_kw` ≈ **761.8 kW** is the rate of gain of this motion energy, not battery or motor input power. **kW** (kilowatts) measures how quickly energy is transferred; it is different from kWh.

The code converts 60 mph to **26.8224 metres per second** and uses **9.80665 m/s²** for standard gravity. For the worked conversion to g, read the [measurement example](testing.md#3-understand-average-peak-and-g).

### 2. Drag: how much power overcomes air resistance?

**Drag** is resistance from moving through air. **CdA**, supplied by `--cda`, combines a drag coefficient (a number describing airflow effects) with the matching reference area. It is not simply the car’s physical area. Here it is an assumed **0.60 square metres (m²)**.

```sh
python3 tools/physics.py drag --speed-mph 230 --cda 0.60
```

The default **air density** is 1.225 kg/m³: 1.225 kg of air per cubic metre of space. The output `aerodynamic_power_kw` is about **399.5 kW**, the power needed just to overcome air resistance at that speed. It excludes tire rolling resistance, uphill driving, motor/gearing losses, fans and accessories.

**Try one change:** replace 230 with **115**, keeping everything else fixed. The result becomes about **49.9 kW**, one eighth as much. In this model, halving speed gives one quarter of the drag and one eighth of the power to overcome it. [NASA drag model](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/)

### 3. Suction: how does pressure produce a push?

Fans can reduce air pressure underneath a car so higher surrounding pressure presses it toward the surface. `--pressure-pa` is the **pressure difference**, not the pressure in a gas tank. A **pascal (Pa)** is one newton per square metre. `--area-m2` is the area over which that difference acts.

```sh
python3 tools/physics.py suction --pressure-pa 5000 --area-m2 3
```

1. Multiply pressure difference by area: **5,000 × 3 = 15,000 N**, or **15 kN** (`force_n`).
2. Divide force by standard gravity: **15,000 ÷ 9.80665 ≈ 1,530 kg** (`equivalent_mass_kg`).

The second number means a force equal to the weight of that mass under standard gravity. It is **not extra vehicle mass**, nor proof that the system can safely hold an upside-down car. The model assumes even pressure and omits leakage, power needs and a margin beyond the minimum required force. See the [engineering explanation](engineering.md#4-fans-can-help-with-grip-even-at-low-speed).

### 4. Range: divide available energy by energy use

**Usable energy** is the battery energy available to operate the car. **Wh/km** means watt-hours used per kilometre; one kWh is 1,000 Wh. This example assumes the same energy use for every kilometre.

```sh
python3 tools/physics.py range --usable-kwh 100 --wh-per-km 200
```

1. Convert available energy: **100 kWh = 100,000 Wh**.
2. Divide by energy use: **100,000 ÷ 200 = 500 km**, about **311 miles** (`range_km` and `range_miles`).

**Try one change:** replace 200 with **250 Wh/km**. The same battery energy now gives **400 km**, about **249 miles**. More energy used per kilometre means less distance.

This is arithmetic, not an official range test or a Roadster battery specification. Real energy use changes with speed, temperature, tires, weather, fans, accessories and the driving schedule. [EPA’s range-test explanation](https://www.epa.gov/greenvehicles/fuel-economy-and-ev-range-testing) describes why official ratings need defined testing.

## What the software does

These are simplified calculations, not a connection to a vehicle or a simulation of its control system. The program rejects invalid inputs, such as zero elapsed time, and numbers too large to calculate reliably. Zero speed or zero pressure difference is allowed where the model supports it. The browser uses the same acceleration equations as Python; it does not include the other three models.

**Optional software check:** from the repository’s top folder, run its automated checks with:

```sh
python3 -m unittest discover -s tests -v
```

Passing software tests checks the calculations and repository consistency; it does not verify Tesla’s vehicle. **Continue learning:** [understand the engineering](engineering.md), [evaluate a performance claim](testing.md), or [choose another topic](start-here.md#where-to-go-next).
