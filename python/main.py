import numpy as np

from dwcpy.tx import tx
from dwcpy.rx import rx
from dwcpy import wireless_transfer

data = [np.random.randint(0, 2) for _ in range(100)]

for n in [0.0000001, 1]:
#for n in [0.0000001, 0.001, 0.01, 0.1, 1, 10, 100]:
    a = tx.BPSK_tx(data)
    a.modulation()
    wt = wireless_transfer.wireless_transfer()
    b = wt.AGWN(a, n)
    b = wt.FadingCh(b)
    c = rx.BPSK_rx(b)
    c.demodulation()

    print(wt.BER(a, c))

    # a = tx.QPSK_tx(data)
    # a.modulation()
    # m = manager.manager()
    # b = m.AGWN(a, n)
    # c = rx.QPSK_rx(b)
    # c.demodulation()

    # print(m.BER(a, c))
