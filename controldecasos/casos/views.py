from django.shortcuts import render,redirect
from controldecasos.forms import Usuarioforms  
from django.contrib.auth.decorators import login_required
from .models import SolicitudSoporte
from .forms import SolicitudSoporteForm
# Create your views here.
@login_required
def casosTemplate(request,id):
    vercaso = SolicitudSoporte.objects.get(id=0)
    peticion = SolicitudSoporte.objects.all() 
    context = {
        "parametro": peticion,
        "parametro2": vercaso,
    }
   
    return render(request, "casos/casos.html", context, )


def formulario(request):
    if request.method == 'POST':
            form = Usuarioforms(request.POST)
            if form.is_valid():
                form.save()
    else: 
        form = Usuarioforms()
        return render(request, 'login.html', {'form': form})
                    
                    

def crearsolicitud_soporte(request):
    if request.method == 'POST':
        form = SolicitudSoporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario')
    else:
        form = SolicitudSoporteForm()
    return render(request, 'casos/crearcaso.html', {'form': form})