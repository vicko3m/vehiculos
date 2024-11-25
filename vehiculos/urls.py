from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/nuevo/', views.vehiculo_crear, name='vehiculo_create'),
    path('vehiculos/<int:pk>/editar/', views.vehiculo_update, name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.vehiculo_delete, name='vehiculo_delete'),
]