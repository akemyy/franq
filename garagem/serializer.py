from rest_framework import serializers
from .models import Veiculo, Garagem
from drf_writable_nested import WritableNestedModelSerializer


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = ['data_cadastro']
        
class GaragemSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    #veiculo = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    veiculo = VeiculoSerializer()
    
class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garagem
        exclude = []


class ListaVeiculosPessoaSerializer(serializers.ModelSerializer):
    veiculo_placa = serializers.ReadOnlyField(source='veiculo.placa')
    class Meta:
        model = Garagem
        fields = ['veiculo_placa']
    def get_periodo(self, obj):
        return obj.get_periodo_display()