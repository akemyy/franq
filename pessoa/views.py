from rest_framework import viewsets, generics
#import pessoa
from pessoa.models import Pessoa, Veiculo, Garagem
from pessoa.serializer import PessoaSerializer, VeiculoSerializer, GaragemSerializer, ListaVeiculosGaragemSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pessoas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as veiculos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class GaragemViewSet(viewsets.ModelViewSet):
    """Exibindo todas as garagens"""
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializer

class ListaVeiculosGaragem(generics.ListAPIView):
    """Listando os veiculos de uma garagem"""
    def get_queryset(self):
        queryset = Garagem.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosGaragemSerializer

#from django.http import JsonResponse
#from .models import Pessoa
# Create your views here.

#def index(request):
#    pessoas = Pessoa.objects.all()

#    dados = {
#        'pessoas' : pessoas
#    }
#    return render(request, 'index.html',dados)
#def pessoa(request):
#    if request.method == 'GET':
#        pessoa = {'id': 1,'nome':'ana'}
#        return JsonResponse(pessoa)