import warnings
import numpy as np
import matplotlib.pyplot as plt

class wireless_transfer(object):
    def __init__(self, delay=[0]):
        self.delay = delay
        
    def GWN(self, sigma):
        return sigma * np.random.randn() + sigma * np.random.randn() * 1j
    
    def AGWN(self, tx, sigma=0.1):
        return [s+self.GWN(sigma) for s in tx.signal]

    def BER(self, tx, rx):
        cnt = 0
        for t, r in zip(tx.data, rx.data):
            if t != r:
                cnt += 1

        return cnt / tx.length 
        
    # TransVersalFilter
    def TVF(self, signal_in, tap):
        len_sig = len(signal_in)
        len_tap = len(tap)

        zeropadding = [0 for _ in range(len_tap-1)]
        padded_signal_in = zeropadding + signal_in + zeropadding

        signal_out = [0 for _ in range(len_sig+len_tap-1)]
        for i in range(len_sig+len_tap-1):
            for s, w in zip(padded_signal_in[i:i+len_tap], reversed(tap)):
                signal_out[i] += s*w

        return signal_out


    def FadingChCoef(self):
        
        def ray():
            return np.sqrt(np.power(np.random.randn(), 2) + np.power(np.random.randn(), 2)) * np.sqrt(0.5)

        def euler(A, p):
            return A*np.sin(p) + 1j * A * np.cos(p)
        # a = []
        # for i in range(1000):
        #     a.append( ray())
        # plt.hist(a)
        # plt.show()

        #TODO
        tap = [0 for i in range(max(self.delay)+5)]
        delta = 0.5
        
        for d in self.delay:
            p_tau = np.exp(d/delta)
            RayleighAmp = ray() * np.sqrt(p_tau)
            Phase = np.random.random() * 2 * 3.141
            tap[d] = euler(RayleighAmp, Phase)
        return tap
            
    def FadingCh(self, signal):
        plt.plot(signal)
        tap = self.FadingChCoef()
        tvf = self.TVF(signal, tap)
        #plt.plot(tvf)
        plt.show()
        return tvf
        
