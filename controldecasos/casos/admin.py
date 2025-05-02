from django.contrib import admin
from .models import (
    SolicitudSoporte, 
    TipoIncidencia
)
# Register your models here.

@admin.register(SolicitudSoporte)
class SolicitudSoporteAdmin(admin.ModelAdmin):
    list_display= [
        'ticket',
        
        'caso_usuario',
        'incidencia',
        'descripcion',
        'creado_en',
        'estado',
    ]


@admin.register(TipoIncidencia)
class TipoIncidenciaAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'nombre',       
    ]