from typing import Any
from ode.base_controller import BaseController

from hello.feature.home.business.get import GETUseCase
from hello.feature.home.business.get_api import GETAPIUseCase
from hello.feature.home.gateway.gateway_injector import GatewayInjector
from hello.feature.home.gateway.presenter import Presenter
from hello.feature.home.domain.models import LogMessage

class PresenterImpl(GatewayInjector, BaseController, Presenter):
    def __init__(self, fetcher_api: GETAPIUseCase, fetcher_db: GETUseCase):
        self.fetcher_api = fetcher_api
        self.fetcher_db = fetcher_db

    def do_fetch_api(self, name :str) -> Any:
        return self.process_use_case(name, self.fetcher_api).value
    
    def do_fetch_db(self, size :int) -> LogMessage:
        return self.process_use_case(size, self.fetcher_db).value