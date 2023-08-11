from django.db import models
from django.core.exceptions import ValidationError

class Laboratorio(models.Model):
    nombre = models.CharField()
    ciudad = models.CharField(default='Sin ciudad')
    pais = models.CharField(default='Sin pais')

    def __str__(self):
        return self.nombre + '' + self.ciudad  + '' + self.pais


class DirectorGeneral(models.Model):
    nombre = models.CharField()
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(default='Sin especialidad')

    def __str__(self):
        return self.nombre + ', ' + str(self.laboratorio) + '' + self.especialidad



#Funcion validadora que evita que se ingresen productos con fecha de creacion previas a 2015
def year_validator(value):
    if value.year < 2015:
        raise ValidationError('El año de fabricación no puede ser antes de 2015.')
    
class Producto(models.Model):
    nombre = models.CharField()
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField (validators=[year_validator])
    p_costo = models.DecimalField(max_digits = 10, decimal_places = 2)
    p_venta = models.DecimalField(max_digits = 10, decimal_places = 2)


    def __str__(self):
        return self.nombre + ', ' + str(self.laboratorio) + ', ' + str(self.f_fabricacion.year) + ', ' + str(self.p_costo) + ', ' + str(self.p_venta)



    


