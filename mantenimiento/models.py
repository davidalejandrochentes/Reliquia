from django.db import models
from datetime import date

class Area(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tamaño = models.CharField(max_length=100, blank=False, null=False)
    encargado = models.CharField(max_length=100, blank=False, null=False)
    teléfono_encargado = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(max_length=500, null=True, blank=True)
    ubicación = models.CharField(max_length=100, null=True, blank=True)
    capacidad = models.CharField(max_length=100, null=True, blank=True)
    tipo_de_área = models.CharField(max_length=100, null=True, blank=True)
    estado_de_ocupación = models.CharField(max_length=100, null=True, blank=True)
    equipamiento = models.CharField(max_length=100, null=True, blank=True)
    tipo_de_mantenimiento = models.CharField(max_length=100, blank=False, null=False)
    fecha_ultimo_mantenimiento = models.DateField(default=date.today, blank=False, null=False)
    intervalo_mantenimiento = models.IntegerField(default=30, blank=False, null=False)

    def dias_restantes_mantenimiento(self):
        dias_pasados = (date.today() - self.fecha_ultimo_mantenimiento).days
        dias_restantes = self.intervalo_mantenimiento - dias_pasados
        return dias_restantes
    
    def __str__(self):
        txt = "Nombre: {}, encargado: {}, ultimo mantenimiento: {}"
        return txt.format(self.nombre, self.encargado, self.fecha_ultimo_mantenimiento)