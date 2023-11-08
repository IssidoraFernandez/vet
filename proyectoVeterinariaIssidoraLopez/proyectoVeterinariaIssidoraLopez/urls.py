"""
URL configuration for proyectoVeterinariaIssidoraLopez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoVetIssidora.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('listadoPacientes/', listadoPacientes, name='listado_pacientes'),
    path('registrarMascota/', registrarMascota, name='registrar_mascota'),
    path('editarMascota/<int:id>', editarMascota, name='editar_mascota'),
    path('eliminarMascota/<int:id>', eliminarMascota, name='eliminar_mascota'),
    path('listadoTratamientos/', listadoTratamientos, name='listado_tratamientos'),
    path('registrarTratamiento/', registroTratamiento, name='registrar_tratamiento'),
]
