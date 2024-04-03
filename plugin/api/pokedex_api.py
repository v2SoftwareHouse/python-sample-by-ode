import requests

class PokedexAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch(self, name):
        url = f"{self.base_url}/pokemon/?name={name}"
        response = requests.get(url)
        return response

    def dumb_request(self):
        url = f"{self.base_url}/test"
        response = requests.get(url)
        return response