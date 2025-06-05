from django.shortcuts import render,redirect, get_object_or_404
from controldecasos.forms import Usuarioforms  
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status



# from .models import SolicitudSoporte

from .serializers import (
    SolicitudSoporteSerializer,
    HistorialEstadoSerializer
)


from .models import (
    SolicitudSoporte,
    TipoIncidencia,
    HistorialEstado,
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
            # console.log(registro)
            console.log(registro.__dict__)
            # console.log(form)
            dataRegistro = registro.__dict__

            solicitudDeSoporte = SolicitudSoporte.objects.get(ticket=dataRegistro['ticket'])
            console.log(solicitudDeSoporte)

            historico = HistorialEstado(
                solicitud_soporte=solicitudDeSoporte,
                estado=dataRegistro['estado'],
               # comentario_usuario=dataRegistro['comentario_usuario'],
                comentario="Solicitud creada",
                usuario = request.user
            )
            
            historico.save()

            console.log(historico)
            
            return JsonResponse({"ok" : "incidencia creada"}, status=201)
            

        # Imprimir errores si los hay
        for field in form:
                if field.errors:
                    print(f"Errores en {field.name}: {field.errors}")

        console.log("no lo cogio")
        
    else:
        form = SolicitudSoporteForm()
    return render(request, 'casos/casos.html', {'form': form})


"""@login_required
def editar_solicitud_soporte(request, ticket):
    solicitud = SolicitudSoporte.objects.get(ticket=ticket)
    
    if request.method == 'POST':
        form = SolicitudSoporteForm(request.POST, instance=solicitud)
        
        if form.is_valid():
            form.save()
            return redirect('casos:casosTemplate')
    else:
        form = SolicitudSoporteForm(instance=solicitud)
    
    return render(request, 'casos/editar_solicitud_soporte.html', {'form': form, 'ticket': ticket})"""

# @login_required
@api_view(['GET', 'POST'])
def VerEstadosTicket(request, ticket=None):



    if ticket is None:
        return JsonResponse({"error": "Ticket no proporcionado"}, status=400)
    # Obtener la solicitud de soporte por ticket
    solicitud = SolicitudSoporte.objects.get(ticket=ticket)
    
    # Obtener el historial de estados relacionado con la solicitud
    historial_estados = HistorialEstado.objects.filter(solicitud_soporte=solicitud).values().order_by('-fecha_cambio')

    
    return Response(historial_estados)


@api_view(['GET', 'POST'])
def actualizarEstadosTicket(request):
    

    console.log(request.data)
    #se obtiene el ticket del formulario
    ticketForm = request.data.get('solicitud_soporte')

    if ticketForm is None:
        return JsonResponse({"error": "Ticket no proporcionado"}, status=400)

    #se obtiene el estado del formulario
    estadoForm = request.data.get('estado')
    console.log(ticketForm)
    
    feedback = request.data.get('comentario')
    console.log(feedback)
    
    usuarioenvia = request.data.get("comentario_usuario")
    console.log(usuarioenvia)
    
    
    #se obtiene el ticket de la base de datos
    obtenTicket = SolicitudSoporte.objects.filter(ticket=ticketForm)
    # console.log(obtenTicket)
    # console.log(obtenTicket[0].estado)
    # console.log(obtenTicket[0].ticket)

    #se hace la actualizacion del estado del ticket
    obtenTicket.update(estado=estadoForm)

    # creacionHistorial = HistorialEstado(
    #     solicitud_soporte=obtenTicket[0],
    #     estado=estadoForm,
    #     comentario=feedback,
    # )
    # creacionHistorial.save()
    
    serializer = HistorialEstadoSerializer(data=request.data,context={'request': request} ,many=False)
    
    if serializer.is_valid():
        console.log("si es valido")
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"ok": "actualizado"}, status=status.HTTP_200_OK)