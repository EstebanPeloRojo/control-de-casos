from django import forms
from usuarios.models import TipoUser  

class Usuarioforms(forms.ModelForm):
    class Meta:
        model = TipoUser
        fields = [
            'id',
            'usuario',
            'tipo' 
        ]