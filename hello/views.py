from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView


from feature.homeList.gateway.presenter import Presenter
from feature.homeList.business.get import GETUseCase
from hello.forms import LogMessageForm
from hello.models import LogMessage
from plugin.feature.homeList.gateway.presenter_impl import PresenterImpl
from plugin.feature.homeList.repository_impl import RepositoryImpl


class HomeListView(ListView, Presenter):
    presenter = PresenterImpl(fetcher=GETUseCase(repo=RepositoryImpl()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return self.do_fetch(size=2)

    def do_fetch(self, size :int) -> LogMessage:
        return self.presenter.do_fetch(size=size)
    
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})
