from django import forms
from usuarios import TipoUser  

class Usuarioforms(forms.ModelForm):
    class meta:
        model = TipoUser
        fields = [
            'id',
            'usuario',
            'tipo' 
        ]