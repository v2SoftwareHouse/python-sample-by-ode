from abc import ABC, abstractmethod
from typing import Any
from hello.feature.home.domain.models import LogMessage

class Presenter(ABC):
    
    @abstractmethod
    def do_fetch_db(self, size:int) -> LogMessage:
        pass

    @abstractmethod
    def do_fetch_api(self, name:str) -> Any:
        pass