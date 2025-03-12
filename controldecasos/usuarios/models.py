from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#modelo de la tabla de usuarios que estaran registrados
class TipoUser(models.Model):
        USER_CHOICES = [
            ('1','Tecnico'),
            ('2','Cliente')
        ]
        id = models.AutoField(primary_key=True)
        usuario = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
        tipo = models.CharField(max_length=20, choices=USER_CHOICES,default=2)
        
        


    

