from django.db import models
from django.utils import timezone
# Create your models here.
#modelo de la tabla de las peticiones
class SolicitudSoporte(models.Model): 
   
    ticket = models.AutoField(primary_key=True)
    caso_usuario =models.CharField(max_length=200)
    incidencia = models.CharField(max_length=255)   
    descripcion = models.TextField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=timezone.now) 
    ESTADOS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES,default='pendiente' )


