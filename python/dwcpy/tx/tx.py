from abc import ABCMeta, abstractmethod
import numpy as np
import sys

from dwcpy.utility import TVF


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
            sys.exit("EXIT:data length shoukd be even")
            
        self.data = data
        self.length = len(data)

    def modulation(self):
        self.signal = []

        def qpsk(x, y):
            tmp = 1 / np.sqrt(2) + 1j / np.sqrt(2)
            if x == 0:
                return tmp if y == 0 else tmp.conjugate()
            else:
                return -1 * tmp.conjugate() if y == 0 else -1 * tmp

        for x, y in zip(self.data[::2], self.data[1::2]):
            self.signal.append(qpsk(x, y))


class OFDM_tx(tx_base):
    def __init__(self, data, n_f):
        if len(data) % n_f != 0:
            sys.exit("EXIT:data length should be divided by n_f")
            
        self.data = data
        self.length = len(data)
        self.n_f = n_f

    def modulation(self):
        self.signal = []

        for i in range(self.length // self.n_f):
            self.signal.append(
                list(
                    map(lambda x: -1 if x == 0 else 1,
                            self.data[self.n_f*i:self.n_f*(i+1)]
                        )
                    )
                )
        print('qqqq')
        print(self.signal)
