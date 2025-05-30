from django import forms
from django.forms.widgets import PasswordInput, Select

class Login(forms.Form):
    usuario = forms.CharField(max_length=50, required=True)
    contrasenia = forms.CharField(widget=forms.PasswordInput(), max_length=20, required=True)
    
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)   
        self.fields['usuario'].widget.attrs.update({'class': 'user'})
        self.fields['usuario'].widget.attrs.update({'placeholder': 'Usuario'})
        self.fields['contrasenia'].widget.attrs.update({'class': 'password'})
        self.fields['contrasenia'].widget.attrs.update({'placeholder': 'Contraseña'})
        