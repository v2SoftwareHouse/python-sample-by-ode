
from plugin.api.pokedex_api import PokedexAPI

class PokedexAPIBuilder:
    def __init__(self, base_url):
        self.base_url = base_url

    def build(self):
        return PokedexAPI(self.base_url)
    

# Exemplo de uso

# pokemon_data = api.get_pokemon("pikachu")
# print(pokemon_data)