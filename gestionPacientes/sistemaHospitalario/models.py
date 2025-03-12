from django.db import models

class sistemaHospitalario(models.Model):
    nombreSistema = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    funcionalidades = models.CharField(max_length=50)
    integracion = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.nombreSistema, self.version)
