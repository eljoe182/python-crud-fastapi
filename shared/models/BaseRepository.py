from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def get_all(self, *args):
        pass

    @abstractmethod
    def get_by_id(self, *args):
        pass

    @abstractmethod
    def store(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass
