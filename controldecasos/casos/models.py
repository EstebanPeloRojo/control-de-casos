from django.db import models
from django.utils import timezone
from django.db.models import DO_NOTHING
# Create your models here.
#modelo de la tabla de las peticiones


class TipoIncidencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    # descripcion = models.TextField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo de Incidencia'
        verbose_name_plural = 'Tipo de Incidencias'

    def __str__(self):
        return self.nombre





class SolicitudSoporte(models.Model): 
    ticket = models.AutoField(primary_key=True)
    
    caso_usuario =models.CharField(max_length=200)
    incidencia = models.ForeignKey(TipoIncidencia, on_delete=DO_NOTHING, related_name='tipo_incidencia')
    descripcion = models.TextField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=timezone.now)
    #FeedbackTecnico = models.ForeignKey()
    ESTADOS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES,default='pendiente' )

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        
    def __str__(self):
        return str(self.ticket)
    
    

class FeedbackTecnico(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=255)
    tecnico = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=timezone.now, null=True, blank=True)
    ticket = models.ForeignKey(SolicitudSoporte, on_delete=models.DO_NOTHING, related_name='feedback_tecnico')



class HistorialEstado(models.Model):
    id = models.AutoField(primary_key=True)
    solicitud_soporte = models.ForeignKey(SolicitudSoporte, on_delete=models.DO_NOTHING, related_name='historial_estado')
    estado = models.CharField(max_length=20)
    # estado_nuevo = models.CharField(max_length=20)
    fecha_cambio = models.DateTimeField(auto_now_add=timezone.now)
    comentario = models.TextField(max_length=255, blank=True, null=True, verbose_name="feedback tecnico")
    usuario =models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Historial de Estado'
        verbose_name_plural = 'Historial de Estados'

    def __str__(self):
        return f"{self.solicitud_soporte.ticket} - {self.estado}"

