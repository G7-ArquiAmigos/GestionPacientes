from django.db import models

from sistemaHospitalario.models import sistemaHospitalario

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    contactoEmergencia = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)
    

class ResultadoEEG(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    eeg_id = models.IntegerField()
    diagnosis = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField()
