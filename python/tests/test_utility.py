import unittest
from dwcpy.utility import *

class TestUtilityUnitTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_Mseqgen(self):
        actual = Mseqgen([1, 0, 0, 1], 15)
        expected = [1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1]
 
        self.assertEqual(expected, actual)

# if __name__ == '__main__':
#     unittest.main()
