from django.contrib import admin

from hello.feature.home.business.get_api import GETAPIUseCase
from plugin.feature.home.repository_api_impl import RepositoryAPIImpl

from .feature.home.domain import models

from hello.feature.home.business.get import GETUseCase
from hello.feature.home.gateway.gateway_injector import GatewayInjector
from plugin.feature.home.gateway.presenter_impl import PresenterImpl
from plugin.feature.home.repository_impl import RepositoryImpl

admin.site.register(models.LogMessage)

useCaseAPI = GETAPIUseCase(repo=RepositoryAPIImpl(url="https://pokeapi.co/api/v2"))
useCaseDB = GETUseCase(repo=RepositoryImpl())

#Inject Presenter with Singleton
GatewayInjector.presenter = PresenterImpl(fetcher_api=useCaseAPI, 
                                          fetcher_db=useCaseDB)