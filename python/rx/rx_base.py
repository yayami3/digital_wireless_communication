from abc import ABCMeta, abstractmethod

class rx_base(object):
    __metaclass__=ABCMeta

    # @abstractmethod
    # def __init__(self, data):
    #     self.data = data
    #     self.len = len(data)

    @abstractmethod
    def demodulation(self):
        raise NotImplementedError()

class BPSK_rx(rx_base):
    def __init__(self, signal):
        self.signal = signal
        # super().__init__(data)
        
    def demodulation(self):
        self.data = list(map(lambda y: 0 if y.real<0 else 1, self.signal)) 
        
class QPSK_rx(rx_base):
    def __init__(self, signal):
        self.signal = signal
        
    def demodulation(self):
        self.data = []
        for s in self.signal:
            if s.real>0:
                self.data.append(0)                
            else:
                self.data.append(1)
                
            if s.imag>0:
                self.data.append(0)
            else:
                self.data.append(1)
