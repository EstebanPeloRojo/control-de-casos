from django.db import models
from django.utils import timezone
from django.db.models import DO_NOTHING
# Create your models here.
#modelo de la tabla de las peticiones



# modelo de datos de los tipos de incidencias
class TipoIncidencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Tipo de Incidencia'
        verbose_name_plural = 'Tipo de Incidencias'

    def __str__(self):
        return self.nombre




#Modelo de datos de las incidencias que se crearan 
class SolicitudSoporte(models.Model): 
    ticket_tilena = models.CharField(max_length=100)
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
    
    



#Modelo de la base de datos donde se guardan los avances de las incidencias incluyendo el estado en el que se encuentra
#comentarios con respecto al caso y la fecha en el que se publica el avance 
class HistorialEstado(models.Model):
    id = models.AutoField(primary_key=True)
    solicitud_soporte = models.ForeignKey(SolicitudSoporte, on_delete=models.DO_NOTHING, related_name='historial_estado')
    estado = models.CharField(max_length=20)
    # estado_nuevo = models.CharField(max_length=20)
    fecha_cambio = models.DateTimeField(auto_now_add=timezone.now)
    comentario = models.TextField(max_length=255, blank=True, null=True, verbose_name="feedback tecnico")
    usuario = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Historial de Estado'
        verbose_name_plural = 'Historial de Estados'

    def __str__(self):
        return f"{self.solicitud_soporte.ticket} - {self.estado}"

