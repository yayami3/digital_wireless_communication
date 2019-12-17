from abc import ABCMeta, abstractmethod

class tx_base(object):
    __metaclass__=ABCMeta

    # @abstractmethod
    # def __init__(self, data):
    #     self.data = data
    #     self.len = len(data)

    @abstractmethod
    def modulation(self):
        raise NotImplementedError()
