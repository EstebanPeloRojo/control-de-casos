from django.shortcuts import render,redirect
from controldecasos.forms import Usuarioforms  
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status


# from .models import SolicitudSoporte

from .serializers import SolicitudSoporteSerializer

from .models import (
    SolicitudSoporte,
    TipoIncidencia,
)
from .forms import SolicitudSoporteForm

from rich.console import Console
console=Console()


# Create your views here.
@login_required
def casosTemplate(request):
    # vercaso = SolicitudSoporte.objects.get(id=0)
    peticion = SolicitudSoporte.objects.all() 

    tiposDeCasos = TipoIncidencia.objects.all()
    context = {
        "parametro": peticion,
        "tiposDeCasos": tiposDeCasos,
        # "parametro2": vercaso,
    }
   
    return render(request, "casos/casos.html", context, )

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

        console.log(request.data)
        console.log(request.query_params)

        id=request.query_params.get('id')
        console.log(id)

        ticket = SolicitudSoporte.objects.filter(ticket=id).values()

        console.log(ticket)

        return Response(ticket[0], status=status.HTTP_200_OK)



    def post(self, request):

        console.log(request.data)
        serializer = SolicitudSoporteSerializer(data=request.data)
        
        if serializer.is_valid():
            # print("si sr si es valido")
            serializer.save()
            return Response({"ok" : "i made a post"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        console.log(request.data)
        id = request.data.get('id')
        console.log(id)

        caso = SolicitudSoporte.objects.get(ticket=id)
        caso.delete()
        
        return Response({"ok" : "deleted"}, status=status.HTTP_204_NO_CONTENT)
                    

@login_required
def crearsolicitud_soporte(request):
    console.log(request.POST)
    if request.method == 'POST':
        
        form = SolicitudSoporteForm(request.POST)

        if form.is_valid():
            registro = form.save(commit=False)
            registro.caso_usuario = request.user
            registro.save()
            
            return JsonResponse({"ok" : "incidencia creada"}, status=201)
            

        # Imprimir errores si los hay
        for field in form:
                if field.errors:
                    print(f"Errores en {field.name}: {field.errors}")

        console.log("no lo cogio")
        
    else:
        form = SolicitudSoporteForm()
    return render(request, 'casos/casos.html', {'form': form})
