from rest_framework import serializers
from .models import *


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da marca'},
            'nome': {'help_text': 'Nome da marca do veículo'},
        }


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do modelo'},
            'nome': {'help_text': 'Nome do modelo do veículo'},
        }


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da unidade de medida'},
            'nome': {'help_text': 'Nome da unidade de medida (Ex: Horas, Km, Litros)'},
        }


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do veículo'},
            'descricao': {'help_text': 'Descrição do veículo'},
            'marca': {'help_text': 'ID da marca (buscar na API Marca)'},
            'modelo': {'help_text': 'ID do modelo (buscar na API Modelo)'},
            'ano': {'help_text': 'Ano de fabricação do veículo'},
            'horimetro': {'help_text': 'Horímetro atual do veículo'},
        }


class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do tipo de medição'},
            'tipo': {'help_text': 'Tipo da medição (Ex: Horímetro, Odômetro, Combustível)'},
            'unidade_medida': {'help_text': 'ID da unidade de medida (buscar na API UnidadeMedida)'},
        }


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da medição do veículo'},
            'veiculo': {'help_text': 'ID do veículo (buscar na API Veiculo)'},
            'medicao': {'help_text': 'ID do tipo de medição (buscar na API Medicao)'},
            'data': {'help_text': 'Data e hora da medição'},
            'valor': {'help_text': 'Valor medido'},
        }