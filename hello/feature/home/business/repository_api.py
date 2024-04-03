from abc import ABC, abstractmethod
from typing import Any

class RepositoryAPI(ABC):
    @abstractmethod
    def do_fetch(self, name: str) -> Any:
        pass
