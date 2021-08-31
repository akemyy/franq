from django.contrib import admin
from garagem.models import Veiculo, Garagem
from pessoa.models import Pessoa


class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'tipo')
    list_display_links = ('id', 'modelo')
    search_fields = ('modelo',)
    list_filter = ('tipo',)
    list_per_page = 20

admin.site.register(Veiculo, ListandoVeiculos)

class ListandoGaragens(admin.ModelAdmin):
    list_display = ('id', 'telefone', 'email')
    list_display_links = ('id', 'email')
    #list_filter = ('tipo',)

admin.site.register(Garagem, ListandoGaragens)

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    #list_filter = ('visivel',)
    list_per_page = 20

admin.site.register(Pessoa, ListandoPessoas)
