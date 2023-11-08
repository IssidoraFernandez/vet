from django.shortcuts import render
from djangoVetIssidora.models import Paciente
from djangoVetIssidora.forms import pacienteRegistrationForm
from djangoVetIssidora.forms import tratamientosRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse	

# Create your views here.
def index(request):
    return render(request, 'djangoVet/index.html')

def listadoPacientes(request):
    paciente = Paciente.objects.all()
    data = {
        'paciente': paciente
    }
    return render(request, 'djangoVet/listamascotas.html', data)



def registrarMascota(request):
    form = pacienteRegistrationForm(request.POST)
    if form.is_valid():
        print("FORMULARIO VALIDO")
        print("Nombre: ", form.cleaned_data['nombre'])
        print("Microchip: ", form.cleaned_data['microchip'])
        print("Fecha de Atencion: ", form.cleaned_data['fecha_de_atencion'])
        print("Motivo de Atencion: ", form.cleaned_data['motivo_de_atencion'])
        print("Diagnostico: ", form.cleaned_data['diagnostico'])
        print("Valor de Consulta: ", form.cleaned_data['valor_consulta'])
        form.save()
        form.cleaned_data['Nombre'] = ''
        form.cleaned_data['Microchip'] = ''
        form.cleaned_data['Fecha de Atencion'] = ''
        form.cleaned_data['Motivo de Atencion'] = ''
        form.cleaned_data['Diagnostico'] = ''
        form.cleaned_data['Valor de Consulta'] = ''
        return HttpResponseRedirect(reverse('listado_pacientes'))
    
    data = {'form': form,
            'titulo': 'Insertar mascota'}
    return render(request, 'djangoVet/formMascota.html', data)

def editarMascota(request, id):
    paciente = Paciente.objects.get(id=id)
    form = pacienteRegistrationForm(instance=paciente)
    if (request.method == 'POST'):
        form = pacienteRegistrationForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listado_pacientes'))
    data = {'form': form}
    return render(request, 'djangoVet/formMascota.html', data)

def eliminarMascota(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return HttpResponseRedirect(reverse('listado_pacientes'))

def listadoTratamientos(request):
    paciente = Paciente.objects.all()
    data = {
        'paciente': paciente
    }
    return render(request, 'djangoVet/tratamientos.html', data)


def registroTratamiento(request):
    form = tratamientosRegistrationForm(request.POST)
    if form.is_valid():
        print("FORMULARIO VALIDO")
        print("Nombre: ", form.cleaned_data['nombre'])
        print("Microchip: ", form.cleaned_data['microchip'])
        print("Tratamiento: ", form.cleaned_data['tratamiento'])
        print("Observación: ", form.cleaned_data['observaciones'])
        print("Valor de tratamiento: ", form.cleaned_data['valor_de_tratamiento'])
        form.save()
        form.cleaned_data['Nombre'] = ''
        form.cleaned_data['Microchip'] = ''
        form.cleaned_data['Tratamiento'] = ''
        form.cleaned_data['Observación'] = ''
        form.cleaned_data['Valor de Consulta'] = ''
        return HttpResponseRedirect(reverse('listado_pacientes'))