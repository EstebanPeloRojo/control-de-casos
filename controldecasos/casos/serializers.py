from rest_framework import routers, serializers, viewsets
from .models import SolicitudSoporte
from .models import HistorialEstado

class SolicitudSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSoporte
        fields = [
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
            'usuario',
        ]
    