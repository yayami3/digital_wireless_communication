import numpy as np

class manager(object):
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
        







