import unittest
from dwcpy.tx import tx
#from context import dwcpy.rx

class TestBPSKRxBaseUnitTest(unittest.TestCase):
    def setUp(self):
        data = [1, 0, 1, 0, 1, 0] 
        self.obj = tx.BPSK_tx(data)

    def test_modulation(self):
        self.obj.modulation()
        actual = self.obj.signal
        expected = [1, -1, 1, -1, 1, -1]  
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
