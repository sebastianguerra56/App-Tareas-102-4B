from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tarea
# Create your views here.

# def inicio(request):
#     return HttpResponse("Hola, esta es mi App de Tareas")

def inicio(request):
    tareas = Tarea.objects.all()

    return render(request, 'tareasapp/inicio.html', {
        'tareas': tareas
    }) 

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
    tarea.delete()
    return redirect('inicio')