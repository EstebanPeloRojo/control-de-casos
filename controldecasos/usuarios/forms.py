from django import forms
from django.forms.widgets import PasswordInput, Select

class Login(forms.Form):
    usuario = forms.CharField(label='user', max_length=50, required=True)
    contrasenia = forms.CharField(widget=forms.PasswordInput(), label='password', max_length=20, required=True)
    
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)   
        self.fields['usuario'].widget.attrs.update({'class': 'user'})
        self.fields['usuario'].widget.attrs.update({'placeholder': 'USER'})
        self.fields['contrasenia'].widget.attrs.update({'class': 'password'})
        self.fields['contrasenia'].widget.attrs.update({'placeholder': 'PASSWORD'})
        