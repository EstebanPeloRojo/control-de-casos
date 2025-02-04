from django.shortcuts import render, redirect
from .forms import Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import messages
# from django.http import HttpResponse
# from django.conf import settings

# Create your views here.
def login_user(request):
    
    message = None

    if request.user.is_authenticated:
        messages.success(request, "Te olvidaste cerrar la sesion?")
        return redirect('/casos/')
    else:
        if request.method == "POST":

            form = Login(request.POST)
            if form.is_valid():
                username = request.POST['usuario']
                password = request.POST['contrasenia']

                print(username)
                print(password)

                user = authenticate(request=request, username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.session['usuario'] = username
                        messages.info(request, "Bienvenido/a "+request.user.first_name+" has iniciado correctamente!")
                        return redirect('/casos/')
                    
                    else:
                        message = "credencial inactiva"
                
                else:
                    message = "Credenciales erroneas o inexistentes, si el error persiste contacte al administrador"
        else:
            form = Login()

        context = {'message': message, 'form':form}
        return render( request, 'usuarios/login.html', context)
    
def logout_user(request):
    logout(request)
    return redirect('/')



