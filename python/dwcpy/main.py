import numpy as np

from dwcpy.tx import tx_base
from dwcpy.rx import rx_base
from dwcpy import wireless_transfer

data = [np.random.randint(0, 2) for _ in range(100)]

for n in [0.0000001, 1]:
#for n in [0.0000001, 0.001, 0.01, 0.1, 1, 10, 100]:
    a = tx_base.BPSK_tx(data)
    a.modulation()
    wt = wireless_transfer.wireless_transfer()
    b = wt.AGWN(a, n)
    b = wt.FadingCh(b)
    c = rx_base.BPSK_rx(b)
    c.demodulation()

    print(wt.BER(a, c))

    # a = tx_base.QPSK_tx(data)
    # a.modulation()
    # m = manager.manager()
    # b = m.AGWN(a, n)
    # c = rx_base.QPSK_rx(b)
    # c.demodulation()

    # print(m.BER(a, c))
