from django.contrib import admin
from .models import SolicitudSoporte
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