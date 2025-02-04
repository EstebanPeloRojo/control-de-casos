from django.shortcuts import render
from controldecasos.forms import Usuarioforms  

# Create your views here.
def index(request):
    context = {
        "parametro": "Esteban",
    }
    return render(request, "index.html", context)

def formulario(request):
    if request.method == 'POST':
            form = Usuarioforms(request.POST)
            if form.is_valid():
                form.save()
    else: 
        form = Usuarioforms()
        return render(request, 'login.html', {'form': form})
                    