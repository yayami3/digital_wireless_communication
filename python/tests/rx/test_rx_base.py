import unittest
from dwcpy.tx import tx_base

class TestTxBaseUnitTest(unittest.TestCase):
    def setUp(self):
        data = [1, 0, 1, 0, 1, 0]
        self.obj = tx_base.BPSK_tx(data)

    def test_modulation(self):
        self.obj.modulation()
        actual = self.obj.signal
        expected = [1, -1, 1, -1, 1, -1] 
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
