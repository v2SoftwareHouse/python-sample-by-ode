
from typing import Any
from plugin.api.api_builder import PokedexAPIBuilder
from plugin.api.base_repository import BaseRepository
from plugin.feature.home.repository_impl import RepositoryImpl

class RepositoryAPIImpl(BaseRepository, RepositoryImpl):
    def __init__(self, url: str):
        super().__init__(url)

    def do_fetch(self, name: str) -> Any:
        return self.get_body_or_throw(self.get_service().fetch(name=name))

    def get_service(self):
        return PokedexAPIBuilder(self.base_url).build()
