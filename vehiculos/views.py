from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/vehiculo_list.html', {
        'vehiculos': vehiculos
    })

def vehiculo_crear(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vehículo registrado exitosamente!')
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/vehiculo_form.html', {
        'form': form,
        'action': 'Crear'
    })

def vehiculo_update(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vehículo actualizado exitosamente!')
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/vehiculo_form.html', {
        'form': form,
        'action': 'Actualizar'
    })

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, '¡Vehículo eliminado exitosamente!')
        return redirect('vehiculo_list')
    return render(request, 'vehiculos/vehiculo_confirm_delete.html', {
        'vehiculo': vehiculo
    })