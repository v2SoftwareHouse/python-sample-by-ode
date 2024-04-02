from abc import ABC, abstractmethod

from hello.models import LogMessage

class Presenter(ABC):
    
    @abstractmethod
    def do_fetch(self) -> LogMessage:
        pass
