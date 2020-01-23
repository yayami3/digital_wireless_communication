import unittest
from dwcpy.utility import *
from dwcpy.wireless_transfer import wireless_transfer
from dwcpy.tx import tx
from dwcpy.rx import rx

class TestWIrelessTransferUnitTest(unittest.TestCase):
    def setUp(self):
        self.wt = wireless_transfer()
        
        self.data1 = [1, 0, 0, 1, 1, 1, 0, 0]
        self.data2 = [1, 0, 1, 1, 0, 1, 0, 0]

        self.tx1 = tx.BPSK_tx(self.data1)
        self.tx1.modulation()

        self.rx1 = rx.BPSK_rx(self.tx1)
        self.rx1.demodulation()

        self.tx2 = tx.BPSK_tx(self.data2)
        self.tx2.modulation()

        self.rx2 = rx.BPSK_rx(self.tx2)
        self.rx2.demodulation()

        
    def test_BER1(self):
        actual = self.wt.BER(self.tx1, self.rx1)
        expected = 0
 
        self.assertEqual(expected, actual)

    def test_BER2(self):
        actual = self.wt.BER(self.tx1, self.rx2)
        expected = 1 / 4
 
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
