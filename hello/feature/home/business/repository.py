from abc import ABC, abstractmethod
from typing import Any

class Repository(ABC):
    @abstractmethod
    def do_fetch(self, size: int) -> Any:
        pass
