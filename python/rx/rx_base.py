from abc import ABCMeta, abstractmethod

class rx_base(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def demodulation(self):
        raise NotImplementedError()

class BPSK_rx(rx_base):
    def __init__(self, signal):
        self.signal = signal
        self.data = None
        
    def demodulation(self):
        self.data = list(map(lambda y: 0 if y.real<0 else 1, self.signal)) 
        
class QPSK_rx(rx_base):
    def __init__(self, signal):
        self.signal = signal
        self.data = None
        
    def demodulation(self):
        self.data = []
        for s in self.signal:
            self.data.append(0 if s.real>0 else 1)
            self.data.append(0 if s.imag>0 else 1)
                
