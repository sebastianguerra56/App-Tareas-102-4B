from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from .models import Tarea
# Create your views here.


def inicio(request):

    return render(request, 'tareasapp/inicio.html') 

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        completada = 'completada' in request.POST
        tarea = Tarea(titulo=titulo, descripcion=descripcion, completada=completada)
        tarea.save()
        return redirect('inicio')
    return render(request, 'tareasapp/crear.html')

def ver_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    return render(request, 'tareasapp/detalle.html', {'tarea': tarea})

def editar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.completada = 'completada' in request.POST  # 👈 clave

        tarea.save()
        return redirect('inicio')
    return render(request, 'tareasapp/editar.html', {'tarea': tarea})

def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
            tarea.delete()
            return redirect('inicio')
    return render(request, 'tareasapp/eliminar.html', {'tarea': tarea})

def login(request):
    return render(request, 'tareasapp/login.html')

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            token, creado = Token.objects.get_or_create(user=usuario)
            return Response({
                'mensaje': 'Autenticacion correcta',
                'usuario': usuario.username,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Usuario o contraseña incorrectos'             
            }, status=status.HTTP_401_UNAUTHORIZED)

class TareasAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    #Get listar todas las tareas
    def get(self, request):
        tareas = Tarea.objects.all()
        datos = []

        for tarea in tareas:
            datos.append({
                'id': tarea.id,
                'titulo': tarea.titulo,
                'descripcion': tarea.descripcion,
                'completada': tarea.completada
            })   
        return Response(datos, status=status.HTTP_200_OK)
