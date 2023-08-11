from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

#Se personaliza la presentacion de los datos en el sitio administrativo de la pagina
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')


@admin.register(DirectorGeneral)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'especialidad')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    
   
   