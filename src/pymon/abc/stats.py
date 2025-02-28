from abc import ABC, abstractmethod
from pymon.core.logger import LoggerMixin


class Stats(LoggerMixin, ABC):
    @abstractmethod
    def validate(self) -> bool:
        raise NotImplementedError
