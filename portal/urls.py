from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("informacoes/", views.info, name="informacoes"),
    path("jogadores/", views.jogadores, name="jogadores"),
    path("conquistas/", views.titulos, name="conquistas"),
]