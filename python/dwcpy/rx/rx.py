from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt

from dwcpy.wireless_transfer import wireless_transfer as wt
from dwcpy.utility import *

class rx_base(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def demodulation(self):
        raise NotImplementedError()

    def inv_ss(self):
        ss_pattern = list(reversed(self.ss_pattern))
        self.signal_iss = TVF(self.ss_rx, ss_pattern)
        self.signal = []
        N_c = self.N_c
        plt.plot(self.signal_iss)
        plt.show()
        for i in range(len(self.signal_iss)//N_c):
            self.signal += [1] if (self.signal_iss[N_c-1+N_c*i].real > 0) else [-1]
        
        
class BPSK_rx(rx_base):
    def __init__(self, tx):
        self.signal = tx.signal
        self.ss_rx = tx.ss_tx
        self.ss_pattern = tx.ss_pattern
        if tx.ss_pattern:
            self.N_c = len(tx.ss_pattern)
        self.data = None
        
    def demodulation(self):
        self.data = list(map(lambda y: 0 if y.real<0 else 1, self.signal)) 
        
class QPSK_rx(rx_base):
    def __init__(self, tx):
        self.signal = tx.signal
        # self.ss_rx = tx.ss_tx
        # self.ss_pattern = tx.ss_pattern
        # if tx.ss_pattern:
        #     self.N_c = len(tx.ss_pattern)
        self.data = None
        
    def demodulation(self):
        self.data = []
        for s in self.signal:
            self.data.append(0 if s.real>0 else 1)
            self.data.append(0 if s.imag>0 else 1)
                
