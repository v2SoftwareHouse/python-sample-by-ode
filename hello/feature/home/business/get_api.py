from typing import Any
from ode.use_case import UseCase
from ode.output import Output
from ode.value_out_put import ValueOutput
from hello.feature.home.business.repository_api import RepositoryAPI

class GETAPIUseCase(UseCase[str, Any]):
    def __init__(self, repo: RepositoryAPI):
        self.repo = repo

    def execute(self, param: str) -> Output[Any]:
        unit = self.repo.do_fetch(param)
        return ValueOutput(unit)
