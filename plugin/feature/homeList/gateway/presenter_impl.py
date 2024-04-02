
from ode.base_controller import BaseController

from feature.homeList.business.get import GETUseCase
from feature.homeList.gateway.gateway_injector import GatewayInjector
from feature.homeList.gateway.presenter import Presenter
from hello.models import LogMessage

class PresenterImpl(GatewayInjector, BaseController, Presenter):
    def __init__(self, fetcher: GETUseCase):
        self.fetcher = fetcher

    def do_fetch(self, size: int) -> LogMessage:
        return self.process_use_case(size, self.fetcher).value