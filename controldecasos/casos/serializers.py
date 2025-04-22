from rest_framework import routers, serializers, viewsets
from .models import SolicitudSoporte


class SolicitudSoporteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SolicitudSoporte
        fields = [
            'ticket',
            'caso_usuario',
            'incidencia',
            'descripcion',
            'estado',
        ]