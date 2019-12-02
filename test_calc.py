import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
        #run python -m unittest test_calc
        #outcome: OK --> test is geslaagd 
 