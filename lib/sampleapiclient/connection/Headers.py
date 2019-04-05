from abc import ABCMeta, abstractmethod


class Headers:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_header_data(self):
        pass

    @abstractmethod
    def set_digest(self):
        pass

    @abstractmethod
    def set_signature(self, date_time, logger):
        pass

    @abstractmethod
    def set_user_agent(self):
        pass

    @abstractmethod
    def set_json_application(self):
        pass
