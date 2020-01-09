from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt

from dwcpy.wireless_transfer import wireless_transfer as wt
from dwcpy.utility import *

class rx_base(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def demodulation(self):
        raise NotImplementedError()

    def inv_ss(self, ss_pattern, N_c):
        N_c = len(ss_pattern)
        ss_pattern = list(reversed(ss_pattern))
        self.signal_iss = TVF(self.signal, ss_pattern)
        plt.plot(self.signal, label="raw")
        plt.plot(self.signal_iss, label="iss")
        plt.legend()
        plt.show()

        self.signal = []
        for i in range(len(self.signal_iss)//6):
            self.signal += [1] if (self.signal_iss[3+6*i].real > 0) else [0]
        print(self.signal)
        
        
        
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
                
