import unittest
from dwcpy.rx import rx

class TestQPSKRxBaseUnitTest(unittest.TestCase):
    def setUp(self):
        signal = [1, -1, 1, -1, 1, -1] 
        self.obj = rx.QPSK_rx(signal)

    def test_modulation(self):
        self.obj.demodulation()
        actual = self.obj.data
        expected = [1, 0, 1, 0, 1, 0]  
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
