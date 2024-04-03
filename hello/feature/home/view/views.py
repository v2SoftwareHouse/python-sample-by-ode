from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView

from hello.feature.home.gateway.gateway_injector import GatewayInjector
from hello.feature.home.gateway.presenter import Presenter
from hello.feature.home.domain.forms import LogMessageForm
from hello.feature.home.domain.models import LogMessage

class HomeListView(ListView, Presenter):
    presenter = GatewayInjector.presenter
    
    def get_queryset(self) -> QuerySet[Any]:
        json = self.do_fetch_api(name="Bulbasaur") #try using api experience
        print(json)

        model = self.do_fetch_db(size=2) #try using db experience
        return model
    
    def do_fetch_db(self, size :int) -> LogMessage:
        return self.presenter.do_fetch_db(size=size)
    
    def do_fetch_api(self, name :str) -> Any:
        return self.presenter.do_fetch_api(name=name)
    
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
