from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse


#tampoco me funciono :(
class LaboratorioViewTest(TestCase):
    def test_reverse(self):
        # Obtener la URL de la vista usando reverse
        url = reverse('mostrar')
        
        # Hacer una solicitud HTTP GET a la URL
        response = self.client.get(url)
        
        # Verifica que la respuesta tiene un código de estado HTTP 200
        self.assertEqual(response.status_code, 200)
        
        # Verifica que se utiliza la plantilla correcta
        self.assertTemplateUsed(response, 'list.html')
        
        # Verifica que el contenido HTML coincida con lo esperado
        self.assertContains(response, 'Lista de laboratorios')  # Supongamos que este texto aparece en la plantilla
        self.assertContains(response, 'Laboratorio 1')  # el nombre de un laboratorio en la lista
        





#este no me funciono :(
class LaboratorioURLTest(TestCase):
    def test_laboratorio_url(self):
        response = self.client.get('/laboratorio/') 
        self.assertEqual(response.status_code, 200)



class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creamos un laboratorio de prueba en la base de datos simulada
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='Pais 1')

    def test_laboratorio_creado_correctamente(self):
        # Recuperamos el laboratorio de prueba de la base de datos simulada
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio 1')
        
        # Verificamos que los datos coincidan con los que creamos en setUpTestData
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'Pais 1')