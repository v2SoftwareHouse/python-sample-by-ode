from requests import Response
from requests.exceptions import RequestException

from ode.authentication_exception import AuthenticationException
from ode.http_exception import HttpException
from ode.internet_connection_exception import InternetConnectionException

from plugin.api.pokedex_api import PokedexAPI


class BaseRepository:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_body_or_throw(self, call :Response):
        try:
            call.raise_for_status()
            json = call.json()
            return json
        except RequestException as e:
            if call.status_code == 401:
                raise AuthenticationException()
            raise HttpException(call.status_code, call.reason)
        except RequestException as e:
            raise InternetConnectionException()

    def get_service(self) -> PokedexAPI:
        raise NotImplementedError("get_service method must be implemented in subclass")

    def dumb_request(self):
        self.get_body_or_throw(self.get_service().dumb_request())