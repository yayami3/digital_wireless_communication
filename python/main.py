from tx import tx_base, BPSK_tx
from rx import rx_base, BPSK_rx
import manager

for n in [0.001, 0.01, 0.1, 1, 10, 100]:
    a = BPSK_tx.BPSK_tx([1,0,0,1])
    a.modulation()
    m = manager.manager()
    b = m.AGWN(a, n)
    c = BPSK_rx.BPSK_rx(b)
    c.demodulation()

    print(a.data)
    print(c.data)
