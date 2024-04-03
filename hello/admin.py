from django.contrib import admin

from . import models

from feature.homeList.business.get import GETUseCase
from feature.homeList.gateway.gateway_injector import GatewayInjector
from plugin.feature.homeList.gateway.presenter_impl import PresenterImpl
from plugin.feature.homeList.repository_impl import RepositoryImpl

admin.site.register(models.LogMessage)

#Inject Presenter with Singleton
GatewayInjector.presenter = PresenterImpl(fetcher=GETUseCase(repo=RepositoryImpl()))