from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name= 'login'),
    path('tareas/', views.inicio, name='inicio'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('detalle/<int:tarea_id>/', views.ver_tarea, name='ver_tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),

    #API login
    path('api/login/', views.LoginAPIView.as_view(), name='api_login'),

    #API Listar Tareas
    path('api/tareas/', views.TareasAPIView.as_view(), name='api_tareas'),

    #API Ver tarea
    path('api/tareas/<int:tarea_id>/', views.TareaDetalleAPIView.as_view(), name='api_tarea_detalle'),
]