import unittest
import math

from dwcpy.tx import tx


class TestQPSKRxBaseUnitTest(unittest.TestCase):
    def setUp(self):
        data = [1, 1, 1, 0, 0, 1, 0, 0]
        self.obj = tx.QPSK_tx(data)

    def test_modulation(self):
        self.obj.modulation()
        actual = self.obj.signal
        expected = [(-1 - 1j) / math.sqrt(2), (-1 + 1j) / math.sqrt(2),
                    (1 - 1j) / math.sqrt(2), (1 + 1j) / math.sqrt(2)]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
