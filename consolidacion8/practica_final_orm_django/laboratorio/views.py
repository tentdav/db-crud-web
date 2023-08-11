from django.shortcuts import render, redirect
from .models import Laboratorio

#vista para ingresar laboratorios
def insert_view(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre = nombre, ciudad = ciudad, pais = pais)
        laboratorio.save()

        return redirect('mostrar/')
    else:
        return render(request, 'insert.html')

#vista para mostrar los laboratorios
def lista_view(request):
    laboratorio = Laboratorio.objects.all()
    return render(request, 'list.html', {'laboratorio':laboratorio})

#vista para editar los laboratoris ya ingresados
def edit_view(request, pk):
    editar = Laboratorio.objects.get(id = pk)
    
    context = {
        'editar': editar
    }
    return render(request=request, template_name= 'edit.html', context=context)

#View que guarda los cambios
def actualizarlaboratorio(request, id):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais= request.POST['pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.id = id
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save()
    return redirect('/laboratorio/mostrar')
    



#vista para eliminar laboratorios
def delete_view(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/laboratorio/mostrar')
    context = {
        'laboratorio': laboratorio,
    }
    return render(request, 'delete.html', context)

    
    

