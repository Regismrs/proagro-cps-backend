from rest_framework import serializers
from .models import ComunicadoCliente, Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nome']


class ComunicadoClienteSerializer(serializers.ModelSerializer):
    evento_descr = serializers.CharField(source="evento.nome", read_only=True)
    class Meta:
        model = ComunicadoCliente
        fields = ['id', 'cpf', 'nome', 'email', 'evento', 'evento_descr', 'lavoura_lat',
                  'lavoura_lon', 'lavoura_tipo', 'lavoura_data_colheita',
                  'inserted_at', 'updated_at', 'is_active']
        
class ComunicadoSimpleSerializer(serializers.ModelSerializer):
    evento_descr = serializers.CharField(source="evento.nome", read_only=True)
    class Meta:
        model = ComunicadoCliente
        fields = ['id', 'cpf', 'nome', 'evento_descr', 'lavoura_tipo', 
                  'lavoura_data_colheita', 'lavoura_lat', 'lavoura_lon', 
                  'inserted_at']
