from abc import ABC, abstractmethod
from hello.feature.home.domain.models import LogMessage

class Repository(ABC):
    @abstractmethod
    def do_fetch(self, size: int) -> LogMessage:
        pass
