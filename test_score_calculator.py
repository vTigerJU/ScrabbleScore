"""Unit test for score calculator"""
import unittest
from score_calculator import ScoreCalculator


class MyTestCase(unittest.TestCase):
    """Unit test class"""
    score_calc = ScoreCalculator()

    def test_calculate(self):
        """Test calculate function"""
        self.assertEqual(14, self.score_calc.calculate("CABBAGE"))
        self.assertNotEqual(10, self.score_calc.calculate("HELLO"))


if __name__ == "__main__":
    unittest.main()
