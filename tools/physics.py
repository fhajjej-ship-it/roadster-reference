#!/usr/bin/env python3
"""Transparent dimensional examples. No measured Roadster inputs are built in."""
import argparse
import json
import math

G0 = 9.80665  # standard gravity, m/s²
MPH_TO_MPS = 0.44704  # exact unit conversion
JOULES_PER_KWH = 3_600_000


def number(value, name, *, zero=False):
    value = float(value)
    if not math.isfinite(value) or value < 0 or (value == 0 and not zero):
        raise ValueError(f"{name} must be finite and {'non-negative' if zero else 'positive'}")
    return value


def finite_results(result):
    if not all(math.isfinite(value) for value in result.values()):
        raise ValueError('scenario exceeds the finite numerical range; use smaller inputs')
    return result


def acceleration(time_s, mass_kg, speed_mph=60):
    """From actual rest; constant acceleration only for distance/force examples."""
    t = number(time_s, 'time_s')
    m = number(mass_kg, 'mass_kg')
    v = number(speed_mph, 'speed_mph', zero=True) * MPH_TO_MPS
    a = v / t
    energy = 0.5 * m * v * v
    return finite_results(dict(speed_mps=v, average_acceleration_mps2=a, average_acceleration_g=a / G0,
                constant_acceleration_distance_m=0.5 * v * t,
                average_net_force_n=m * a, kinetic_energy_kwh=energy / JOULES_PER_KWH,
                average_kinetic_power_kw=energy / t / 1000))


def drag(speed_mph, cda_m2, density_kg_m3=1.225):
    """Steady aerodynamic drag only; no rolling resistance, fans or drivetrain loss."""
    v = number(speed_mph, 'speed_mph', zero=True) * MPH_TO_MPS
    cda = number(cda_m2, 'cda_m2', zero=True)
    rho = number(density_kg_m3, 'density_kg_m3')
    force = 0.5 * rho * cda * v * v
    return finite_results(dict(drag_force_n=force, aerodynamic_power_kw=force * v / 1000))


def suction(pressure_pa, area_m2):
    """Uniform pressure difference over an effective area; leakage not modeled."""
    force = number(pressure_pa, 'pressure_pa', zero=True) * number(area_m2, 'area_m2')
    return finite_results(dict(force_n=force, equivalent_mass_kg=force / G0))


def range_estimate(usable_kwh, wh_per_km):
    """Constant consumption scenario, not an EPA/WLTP test or certified range."""
    km = 1000 * number(usable_kwh, 'usable_kwh') / number(wh_per_km, 'wh_per_km')
    return finite_results(dict(range_km=km, range_miles=km / 1.609344))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='scenario', required=True)
    a = sub.add_parser('acceleration')
    a.add_argument('--time', type=float, required=True)
    a.add_argument('--mass', type=float, required=True)
    a.add_argument('--speed-mph', type=float, default=60)
    d = sub.add_parser('drag')
    d.add_argument('--speed-mph', type=float, required=True)
    d.add_argument('--cda', type=float, required=True)
    d.add_argument('--density', type=float, default=1.225)
    s = sub.add_parser('suction')
    s.add_argument('--pressure-pa', type=float, required=True)
    s.add_argument('--area-m2', type=float, required=True)
    r = sub.add_parser('range')
    r.add_argument('--usable-kwh', type=float, required=True)
    r.add_argument('--wh-per-km', type=float, required=True)
    args = parser.parse_args()
    try:
        if args.scenario == 'acceleration':
            result = acceleration(args.time, args.mass, args.speed_mph)
        elif args.scenario == 'drag':
            result = drag(args.speed_mph, args.cda, args.density)
        elif args.scenario == 'suction':
            result = suction(args.pressure_pa, args.area_m2)
        else:
            result = range_estimate(args.usable_kwh, args.wh_per_km)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(dict(scenario=args.scenario, interpretation='Hypothetical educational model; not measured Roadster performance.',
                         inputs=vars(args), results=result), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
