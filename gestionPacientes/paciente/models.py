from django.db import models

from sistemaHospitalario.models import sistemaHospitalario

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    contactoEmergencia = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    sistemaHospitalario = models.ForeignKey(sistemaHospitalario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.nombre)