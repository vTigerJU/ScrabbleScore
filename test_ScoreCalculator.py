import unittest
from score_calculator import ScoreCalculator

class MyTestCase(unittest.TestCase):
    score_calc = ScoreCalculator()

    def test_calculate(self):
        self.assertEqual(8,self.score_calc.calculate("WORD"))
        self.assertNotEqual(10,self.score_calc.calculate("HELLO"))


if __name__ == "__main__":
    unittest.main()
