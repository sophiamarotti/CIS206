import unittest
from bmi import calculate_bmi, bmi_category


class TestBMI(unittest.TestCase):

    # Test 1 — Normal weight
    def test_normal_bmi(self):
        self.assertAlmostEqual(calculate_bmi(150, 65), 24.96, places=2)

    # Test 2 — Underweight
    def test_underweight_bmi(self):
        self.assertAlmostEqual(calculate_bmi(100, 68), 15.2, places=1)

    # Test 3 — Obese category
    def test_obese_category(self):
        bmi = calculate_bmi(200, 64)
        self.assertEqual(bmi_category(bmi), "Obese")

    # Test 4 — Failed condition: zero height
    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(150, 0)

    # Test 5 — Failed condition: negative weight
    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-120, 65)


if __name__ == "__main__":
    unittest.main()
