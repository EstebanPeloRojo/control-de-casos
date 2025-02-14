from django.db import models

# Create your models here.
#modelo de la tabla de las peticiones
class SolicitudSoporte(models.Model): 
   
    ticket = models.IntegerField(primary_key=True)
    caso_usuario =models.CharField(max_length=200)
    incidencia = models.CharField(max_length=255)   
    descripcion = models.TextField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True) 
    ESTADOS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES,default='pendiente' )


