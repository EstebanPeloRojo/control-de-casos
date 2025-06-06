from rest_framework import routers, serializers, viewsets
from .models import SolicitudSoporte
from .models import HistorialEstado

class SolicitudSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSoporte
        fields = [
            'ticket_tilena',
            'ticket',
            'caso_usuario',
            'incidencia',
            'descripcion',
            'estado',
        ]


class HistorialEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstado
        fields = [
            'solicitud_soporte',
            'estado',
            'comentario',
            
        ]
    
    def create(self, validated_data):
        # Obtener el usuario del contexto de la request
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)