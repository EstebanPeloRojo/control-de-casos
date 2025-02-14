from django import forms
from .models import SolicitudSoporte

class SolicitudSoporteForm(forms.ModelForm):
    class Meta:
        model = SolicitudSoporte
        fields = ('ticket', 
                  'caso_usuario',
                  'incidencia',
                  'descripcion',
                  'estado'
                  
                  
                  )
        