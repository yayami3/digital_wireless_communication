from rx import rx_base

class BPSK_rx(rx_base.rx_base):
    def __init__(self, signal):
        self.signal = signal
        # super().__init__(data)
        
    def demodulation(self):
        self.data = list(map(lambda y: 0 if abs(y+1)<abs(y-1) else 1, self.signal)) 
        
