
import django_filters
from rest_framework import viewsets, generics, filters
from rest_framework import permissions
#import pessoa
from pessoa.models import Pessoa
from garagem.models import Veiculo, Garagem
from pessoa.serializer import PessoaSerializer
from garagem.serializer import VeiculoSerializer, GaragemSerializer, ListaVeiculosPessoaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class VeiculoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as veiculos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class GaragemViewSet(viewsets.ModelViewSet):
    """Exibindo todas as garagens"""
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['email']
    search_fields = ['email', 'telefone']
    filterset_fields = ['ativa']

class PessoaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pessoas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaVeiculosPessoa(generics.ListAPIView):
    """Listando os veiculos de uma garagem"""
    def get_queryset(self):
        queryset = Garagem.objects.filter(email=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosPessoaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
#class AddVeiculosGaragem(generics.ListAPIView):
#    """Listando os veiculos de uma garagem"""
#    def get_queryset(self):
#        queryset = Garagem.objects.filter(veiculo_id=self.kwargs['pk'])
#        return queryset
#    serializer_class = AddVeiculosGaragem
