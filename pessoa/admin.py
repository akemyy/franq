from django.contrib import admin
from .models import Pessoa, Veiculo, Garagem


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    #list_filter = ('visivel',)
    list_per_page = 20

admin.site.register(Pessoa, ListandoPessoas)

class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'tipo')
    list_display_links = ('id', 'modelo')
    search_fields = ('modelo',)
    list_filter = ('tipo',)
    list_per_page = 20

admin.site.register(Veiculo, ListandoVeiculos)


class ListandoGaragens(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'veiculo')
    list_display_links = ('id', 'pessoa', 'veiculo')
    search_fields = ('placa',)
    #list_filter = ('tipo',)
    #list_per_page = 20

admin.site.register(Garagem, ListandoGaragens)