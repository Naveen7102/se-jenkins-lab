#!/usr/bin/python3
# Test case for power
import unittest

from power import power

class Testpower(unittest.TestCase):
    def test_list_int(self):
        base = 2
        power = 3
        result=power(base, power)
        self.assertEqual(result,8)

if __name__ == '__main__':
    unittest.main()
