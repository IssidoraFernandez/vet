from django import forms
from djangoVetIssidora.models import Paciente, Tratamientos
from django.core import validators


class pacienteRegistrationForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    microchip = forms.CharField(max_length=50)
    fecha_de_atencion = forms.CharField(max_length=50)
    motivo_de_atencion = forms.CharField(max_length=50)
    diagnostico = forms.CharField(max_length=100)
    valor_consulta = forms.CharField(max_length=50)
    
    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_de_atencion.widget.attrs['class'] = 'form-control'
    motivo_de_atencion.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    valor_consulta.widget.attrs['class'] = 'form-control'



class pacienteRegistrationForm(forms.ModelForm):

    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50),
            validators.RegexValidator('^[A-Za-z0-9ñÑáéíóúÁÉÍÓÚ ]*$', 'Ingrese un nombre valido', 'invalid_nombre')
        ]
    )
    microchip = forms.CharField(
        validators=[
            validators.MinLengthValidator(15),
            validators.MaxLengthValidator(16),
            validators.RegexValidator('^[0-9]*$') 
        ]
    )
    fecha_de_atencion = forms.CharField(max_length=50)
    motivo_de_atencion = forms.CharField(max_length=50)
    diagnostico = forms.CharField(max_length=100)
    valor_consulta = forms.CharField(
        validators=[
            validators.MinLengthValidator(4),
            validators.MaxLengthValidator(7),
            validators.RegexValidator('^[0-9]*$') 
        ]
    )

    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_de_atencion.widget.attrs['class'] = 'form-control'
    motivo_de_atencion.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    valor_consulta.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Paciente
        fields = '__all__'



class tratamientosRegistrationForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    microchip = forms.CharField(max_length=50)
    tratamiento = forms.CharField(max_length=100)
    observaciones = forms.CharField(max_length=150)
    valor_de_tratamiento = forms.CharField(max_length=50)

    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    tratamiento.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    valor_de_tratamiento.widget.attrs['class'] = 'form-control'


class tratamientosRegistrationForm(forms.ModelForm):

    nombre = forms.CharField(max_length=50)
    microchip = forms.CharField(max_length=50)
    tratamiento = forms.CharField(max_length=100)
    observaciones = forms.CharField(max_length=150)
    valor_de_tratamiento = forms.CharField(max_length=50)

    class Meta:
        model = Tratamientos
        fields = '__all__'