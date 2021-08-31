from django.contrib import admin
from django.urls import path, include
from api.views import PessoaViewSet, VeiculoViewSet, GaragemViewSet, ListaVeiculosGaragem
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoaViewSet, basename='Pessoa' )
router.register('veiculos', VeiculoViewSet, basename='Veiculo' )
router.register('garagens', GaragemViewSet, basename='garagem' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('garagem/<int:pk>/veiculos/', ListaVeiculosGaragem.as_view())
]
