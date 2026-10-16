from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name= 'login'),
    path('tareas/', views.inicio, name='inicio'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('tarea/<int:tarea_id>/', views.ver_tarea, name='ver_tarea'),
    path('tarea/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),

    #API login
    path('api/login/', views.LoginAPIView.as_view(), name='api_login'),
]