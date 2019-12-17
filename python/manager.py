import numpy as np

class manager(object):
    def GWN(self, sigma):
        return sigma * np.random.randn() + sigma * np.random.randn() * 1j
    
    def AGWN(self, tx, sigma=0.1):
        print(tx.signal[1]+self.GWN(sigma))
        return [s+self.GWN(sigma) for s in tx.signal]










