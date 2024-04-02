
from feature.homeList.business.repository import Repository
from hello.models import LogMessage

class RepositoryImpl(Repository):
    def __init__(self):
        super().__init__()

    def do_fetch(self, size: int) -> LogMessage:
        return LogMessage.objects.order_by("-log_date")[:size]
