#!/usr/bin/python3
# Test case for power
import unittest

from power import power

class Testpower(unittest.TestCase):
    def test_list_int(self):
        b = 2
        p = 3
        lst = [b,p]
        result=power(lst)
        self.assertEqual(result,8)

if __name__ == '__main__':
    unittest.main()
