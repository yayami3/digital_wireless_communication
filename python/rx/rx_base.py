from abc import ABCMeta, abstractmethod

class rx_base(object):
    __metaclass__=ABCMeta

    # @abstractmethod
    # def __init__(self, data):
    #     self.data = data
    #     self.len = len(data)

    @abstractmethod
    def demodulation(self):
        raise NotImplementedError()
