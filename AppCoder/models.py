from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    edad = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
