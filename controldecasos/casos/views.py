from django.shortcuts import render
from controldecasos.forms import Usuarioforms  
from django.contrib.auth.decorators import login_required



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


from .models import SolicitudSoporte

from .serializers import SolicitudSoporteSerializer





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
                    


class Casos(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        
        return Response({"ok" : "ok"})



    def post(self, request):

        # print(request.data)
        serializer = SolicitudSoporteSerializer(data=request.data)
        
        if serializer.is_valid():
            # print("si sr si es valido")
            serializer.save()
        return Response({"ok" : "i made a post"})
