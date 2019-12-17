from tx import tx_base

class BPSK_tx(tx_base.tx_base):
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        # super().__init__(data)
        
    def modulation(self):
        self.signal = list(map(lambda x: -1 if x==0 else 1, self.data)) 
        
