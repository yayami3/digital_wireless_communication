from tx import tx_base, BPSK_tx

a = BPSK_tx.BPSK_tx([1,0,0,1])
a.modulation()

print(a.signal)
