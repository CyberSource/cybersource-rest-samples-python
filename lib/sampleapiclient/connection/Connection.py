from abc import ABCMeta, abstractmethod


class Connection:
    __metaclass__ = ABCMeta

    @abstractmethod
    def open_connection(self, mconfig, header, proxies):
        pass

    @abstractmethod
    def set_proxy_connection(self):
        pass
