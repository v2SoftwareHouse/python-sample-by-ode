
from hello.feature.home.business.repository import Repository
from hello.feature.home.domain.models import LogMessage
from typing import Any

class RepositoryImpl(Repository):
    
    def do_fetch(self, size: int) -> Any:
        return LogMessage.objects.order_by("-log_date")[:size]