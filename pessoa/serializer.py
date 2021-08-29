from rest_framework import serializers
from pessoa.models import Pessoa, Veiculo, Garagem

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email', 'telefone']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'tipo', 'modelo', 'ano_veiculo', 'cor']
        
class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garagem
        exclude = []

class ListaVeiculosGaragemSerializer(serializers.ModelSerializer):
    veiculo_placa = serializers.ReadOnlyField(source='veiculo.placa')
    class Meta:
        model = Garagem
        fields = ['veiculo_placa']
    def get_periodo(self, obj):
        return obj.get_periodo_display()