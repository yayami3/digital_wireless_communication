from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

from dwcpy.wireless_transfer import wireless_transfer as wt
from dwcpy.utility import *   

class tx_base(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def modulation(self):
        raise NotImplementedError()

    def ss(self, ss_pattern, N_c):
        self.ss_pattern = ss_pattern
        self.N_c = len(ss_pattern)
        self.signal_ss = []
        for d in self.signal:
            self.signal_ss += [d] + [0 for _ in range(self.N_c)]
        self.signal_ss2 = TVF(self.signal_ss, ss_pattern) 
        # plt.plot(self.signal_ss, label="raw")
        # plt.plot(self.signal_ss2, label="tvf")
        # plt.legend()
        # plt.show()
        self.signal = self.signal_ss2
        
class BPSK_tx(tx_base):
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        # super().__init__(data)
        
    def modulation(self):
        self.signal = list(map(lambda x: -1 if x==0 else 1, self.data))

    # def ss(self, ss_pattern, N_c):
    #     super(BPSK_tx, self).ss(ss_pattern, N_c)
        
class QPSK_tx(tx_base):
    def __init__(self, data):
        if len(data) % 2==1:
            print("data length shoukd be even")
            return 0
            
        self.data = data        
        self.length = len(data)
        
    def modulation(self):
        self.signal = [] 
        for i in range(self.length//2):
            tmp = 1/np.sqrt(2) + 1j/np.sqrt(2)
            if self.data[2*i] == 0:
                if self.data[2*i+1] == 0:
                    self.signal.append(tmp) 
                else:                    
                    self.signal.append(tmp.conjugate()) 
            else:
                if self.data[2*i+1] == 0:
                    self.signal.append(-1*tmp.conjugate()) 
                else:
                    self.signal.append(-1*tmp) 

