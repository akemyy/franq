from rest_framework import viewsets, generics
#import pessoa
from pessoa.models import Pessoa
from garagem.models import Veiculo, Garagem
from pessoa.serializer import PessoaSerializer
from garagem.serializer import VeiculoSerializer, GaragemSerializer, ListaVeiculosGaragemSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as veiculos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class GaragemViewSet(viewsets.ModelViewSet):
    """Exibindo todas as garagens"""
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pessoas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class ListaVeiculosGaragem(generics.ListAPIView):
    """Listando os veiculos de uma garagem"""
    def get_queryset(self):
        queryset = Garagem.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosGaragemSerializer
    
    
#class AddVeiculosGaragem(generics.ListAPIView):
#    """Listando os veiculos de uma garagem"""
#    def get_queryset(self):
#        queryset = Garagem.objects.filter(veiculo_id=self.kwargs['pk'])
#        return queryset
#    serializer_class = AddVeiculosGaragem
