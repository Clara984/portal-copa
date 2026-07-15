from django.contrib import admin
from .models import Selecao, Jogador, Titulo


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ("numero", "nome", "posicao", "clube", "idade", "capitao")
    list_filter = ("posicao", "capitao")
    search_fields = ("nome", "clube")


@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ("competicao", "ano", "resultado")
    search_fields = ("competicao",)


@admin.register(Selecao)
class SelecaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "pais", "continente", "tecnico")