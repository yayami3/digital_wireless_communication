import numpy as np
import matplotlib.pyplot as plt

from dwcpy.tx import tx
from dwcpy.rx import rx
from dwcpy import wireless_transfer
from dwcpy.utility import *

data = [np.random.randint(0, 2) for _ in range(30)]
data = [0 for _ in range(20)]

for n in [0.00000001, 0.9]:
#for n in [0.0000001, 0.001, 0.01, 0.1, 1, 10, 100]:
    ss_pt = [1, 0, 0, 1]
    ss_pt = Mseqgen([1, 0, 0, 1], 15)
    print("-----------------------------")
    print(ss_pt)
    
    a = tx.BPSK_tx(data)
    a.modulation()
    a.ss(ss_pt)
    wt = wireless_transfer.wireless_transfer()
    #wt.AGWN(a, n)
    # plt.plot(a.signal, label="noised")
    # plt.legend()
    # plt.show()

    
    #b = wt.FadingCh(b)
    c = rx.BPSK_rx(a)
    c.inv_ss()
    c.demodulation()
    
    print(wt.BER(a, c))

    # a = tx.QPSK_tx(data)
    # a.modulation()
    # m = manager.manager()
    # b = m.AGWN(a, n)
    # c = rx.QPSK_rx(b)
    # c.demodulation()

    # print(m.BER(a, c))
