from abc import ABCMeta, abstractmethod
import numpy as np

# from dwcpy.wireless_transfer import wireless_transfer as wt
from dwcpy.utility import *


class tx_base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modulation(self):
        raise NotImplementedError()

    def ss(self, ss_pattern):
        self.ss_pattern = ss_pattern
        self.N_c = len(ss_pattern)
        signal_ss_pre = []
        for d in self.signal:
            signal_ss_pre += [d] + [0 for _ in range(self.N_c - 1)]
        self.ss_tx = TVF(signal_ss_pre, ss_pattern)


class BPSK_tx(tx_base):
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.signal = None
        self.ss_tx = None
        self.ss_pattern = None

    def modulation(self):
        self.signal = list(map(lambda x: -1 if x == 0 else 1, self.data))


class QPSK_tx(tx_base):
    def __init__(self, data):
        if len(data) % 2 == 1:
            print("data length shoukd be even")
            return 0

        self.data = data
        self.length = len(data)

    def modulation(self):
        self.signal = []
        for i in range(self.length // 2):
            tmp = 1 / np.sqrt(2) + 1j / np.sqrt(2)
            if self.data[2 * i] == 0:
                if self.data[2 * i + 1] == 0:
                    self.signal.append(tmp)
                else:
                    self.signal.append(tmp.conjugate())
            else:
                if self.data[2 * i + 1] == 0:
                    self.signal.append(-1 * tmp.conjugate())
                else:
                    self.signal.append(-1 * tmp)
