from abc import ABC, abstractmethod


class BaseDataManipulator(ABC):
    @classmethod
    @abstractmethod
    def init(cls, *args) -> None:
        pass

    @classmethod
    @abstractmethod
    def data_as_tuple(cls) -> tuple:
        pass

    @classmethod
    @abstractmethod
    def data(cls):
        pass

    @classmethod
    @abstractmethod
    def clear(cls) -> None:
        pass