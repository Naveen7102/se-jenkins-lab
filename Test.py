#!/usr/bin/python3
# Test case for power
import unittest

from power import power

class Testpower(unittest.TestCase):
    def test_list_int(self):
        b = 2.0
        p = 3.0
        result=power(b, p)
        self.assertEqual(result,8.0)

if __name__ == '__main__':
    unittest.main()
