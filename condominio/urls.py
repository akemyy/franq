from django.contrib import admin
from django.urls import path, include
from api.views import PessoaViewSet, VeiculoViewSet, GaragemViewSet, ListaVeiculosPessoa
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoaViewSet, basename='Pessoa' )
router.register('veiculos', VeiculoViewSet, basename='Veiculo' )
router.register('garagens', GaragemViewSet, basename='garagem' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pessoa/<str:pk>/veiculos/', ListaVeiculosPessoa.as_view())
]
