from django.shortcuts import render
from .models import Jogador, Titulo

# Create your views here.
def home(request):
    return render(request, "portal/home.html")

def info(request):
    return render(request, "portal/informacoes.html")

def jogadores(request):

    jogadores = Jogador.objects.order_by("numero")

    return render(request, "portal/jogadores.html", {
        "jogadores": jogadores
    })

def titulos(request):

    titulos = Titulo.objects.all()

    return render(request, "portal/conquistas.html", {
        "titulos": titulos
    })