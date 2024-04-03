from typing import Any
from ode.use_case import UseCase
from ode.output import Output
from ode.value_out_put import ValueOutput
from hello.feature.home.business.repository import Repository
from hello.feature.home.domain.models import LogMessage

class GETUseCase(UseCase[int, LogMessage]):
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, param: int) -> Output[LogMessage]:
        unit = self.repo.do_fetch(param)
        return ValueOutput(unit)
