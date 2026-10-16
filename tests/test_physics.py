import math
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from physics import acceleration, drag, range_estimate, suction
from validate import validate


class PhysicsTests(unittest.TestCase):
    def test_exact_speed_conversion(self):
        self.assertAlmostEqual(acceleration(1, 1)['speed_mps'] * 3.6, 96.56064)

    def test_independent_acceleration_example(self):
        r = acceleration(2, 1000, 60)
        self.assertAlmostEqual(r['average_acceleration_mps2'], 13.4112)
        self.assertAlmostEqual(r['constant_acceleration_distance_m'], 26.8224)
        self.assertAlmostEqual(r['average_net_force_n'], 13411.2)
        self.assertAlmostEqual(r['kinetic_energy_kwh'], 0.0999223808)

    def test_force_and_energy_scale_with_mass(self):
        one, two = acceleration(2, 1000), acceleration(2, 2000)
        self.assertEqual(one['average_acceleration_g'], two['average_acceleration_g'])
        self.assertEqual(two['kinetic_energy_kwh'], 2 * one['kinetic_energy_kwh'])

    def test_drag_power_cubic_scaling(self):
        one, two = drag(100, 0.6), drag(200, 0.6)
        self.assertAlmostEqual(two['drag_force_n'] / one['drag_force_n'], 4)
        self.assertAlmostEqual(two['aerodynamic_power_kw'] / one['aerodynamic_power_kw'], 8)

    def test_pressure_area_dimensions(self):
        self.assertEqual(suction(5000, 3)['force_n'], 15000)

    def test_energy_consumption_range(self):
        result = range_estimate(100, 200)
        self.assertEqual(result['range_km'], 500)
        self.assertAlmostEqual(result['range_miles'], 310.685596118667)

    def test_invalid_denominators_and_nonfinite_inputs(self):
        for value in (0, -1, math.nan, math.inf, -math.inf):
            with self.subTest(value=value), self.assertRaises(ValueError):
                acceleration(value, 1000)
            with self.subTest(value=value), self.assertRaises(ValueError):
                range_estimate(100, value)

    def test_zero_motion_and_pressure(self):
        self.assertEqual(drag(0, 0.6)['aerodynamic_power_kw'], 0)
        self.assertEqual(acceleration(1, 1000, 0)['average_net_force_n'], 0)
        self.assertEqual(suction(0, 3)['force_n'], 0)

    def test_repository_evidence_integrity(self):
        self.assertEqual(validate(), [])


if __name__ == '__main__':
    unittest.main()
