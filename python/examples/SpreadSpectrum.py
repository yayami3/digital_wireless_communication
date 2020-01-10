from dwcpy.tx import tx
from dwcpy.rx import rx
from dwcpy.utility import *

if __name__ == "__main__":
    data = [0 for _ in range(20)]
    ss_pt = Mseqgen([1, 0, 0, 1], 15)
    print("-----------------------------")
    print(ss_pt)

    a = tx.BPSK_tx(data)
    a.modulation()
    a.ss(ss_pt)

    c = rx.BPSK_rx(a)
    c.inv_ss()
    c.demodulation()


