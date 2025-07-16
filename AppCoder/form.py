from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Alumno(forms.Form):    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    documento = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    email = forms.EmailField()
    edad = forms.IntegerField()

class Profesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    documento = forms.IntegerField()
    email = forms.EmailField()
