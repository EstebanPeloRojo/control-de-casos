from django import forms
from .models import SolicitudSoporte

class SolicitudSoporteForm(forms.ModelForm):
    class Meta:
        model = SolicitudSoporte
        
        fields = ( 
                  
                  'incidencia',
                  'descripcion',
                  'estado'          
                  )
        exclude = ('caso_usuario',)   
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].widget = forms.Select(choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('resuelto', 'Resuelto'),
        ])
        