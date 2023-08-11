from django.contrib import  admin
from django.urls import path, include
from . import views

#urls de la app
urlpatterns = [
    path('mostrar/', views.lista_view , name = 'mostrar'),
    path('insertar/',views.insert_view , name = 'insertar'),
    path('editar/<int:pk>', views.edit_view , name = 'editar'),
    path('editar/actualizarlaboratorio/<int:pk>', views.actualizarlaboratorio, name='actualizarlaboratorio'),
    path('eliminar/<int:pk>', views.delete_view , name = 'eliminar'),

]