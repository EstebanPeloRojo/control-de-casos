from django.shortcuts import render
from controldecasos.forms import Usuarioforms  
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def casosTemplate(request):
    context = {
        "parametro": "Esteban",
    }
    
    return render(request, "casos/casos.html", context)

def CrearCaso(request):
    return render(request, 'casos/CrearCaso.html')

def prueba(request):
    #pass
    return render(request, 'casos/prueba.html',)

def formulario(request):
    if request.method == 'POST':
            form = Usuarioforms(request.POST)
            if form.is_valid():
                form.save()
    else: 
        form = Usuarioforms()
        return render(request, 'login.html', {'form': form})
                    