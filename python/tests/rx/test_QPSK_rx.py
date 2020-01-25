import unittest
from dwcpy.tx import tx
from dwcpy.rx import rx


class TestRxBaseUnitTest(unittest.TestCase):
    def setUp(self):
        data = [1, 0, 1, 0, 1, 0]
        tx_module = tx.QPSK_tx(data)
        tx_module.modulation()
        self.obj = rx.QPSK_rx(tx_module)

    def test_modulation(self):
        self.obj.demodulation()
        actual = self.obj.data
        expected = [1, 0, 1, 0, 1, 0]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
