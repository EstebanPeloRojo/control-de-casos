from django.db import models 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
#modelo de la tabla de usuarios que estaran registrados        

    

class TipoUser(models.Model):
        USER_CHOICES = [
            ('1','Tecnico'),
            ('2','operativo'),
            ("3","administrador"),
            ("4","directivo"),
        ]
        id = models.AutoField(primary_key=True)
        usuario = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
        tipo = models.CharField(max_length=20, choices=USER_CHOICES,default=2)  

        def __str__(self):
            return self.nombre

class DatosUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='datos_usuario')
    doc_identidad = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=100, blank=False, null=False)
    
    


   