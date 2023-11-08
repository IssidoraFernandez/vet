from django.db import models

# Create your models here.
class Tratamientos(models.Model):
    nombre = models.CharField(max_length=50)
    microchip = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=150)
    valor_de_tratamiento = models.CharField(max_length=50)
    
    def __str__(self):
        return self.microchip

    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    microchip = models.ForeignKey(Tratamientos, on_delete=models.CASCADE)
    fecha_de_atencion = models.DateField(max_length=50)
    motivo_de_atencion = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=100)
    valor_consulta = models.CharField(max_length=50)



    