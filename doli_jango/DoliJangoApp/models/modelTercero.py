from django.db import models
from unidecode import unidecode
from django.utils import timezone


class Tercero(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=9, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    provincia = models.CharField(max_length=200)
    poblacion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    tarjeta_id = models.CharField(max_length=16, unique=True, null=True, blank=True)  # ID de la tarjeta

    def __str__(self):
        return f"{self.nombre} {self.apellidos}  {self.email}"
    
    def save(self, *args, **kwargs):
        # Validar que la población pertenece a la provincia seleccionada
        #poblaciones_validas = dict(POBLACIONES_CHOICES).get(self.provincia, [])
        #poblacion_nombres = [p[0] for p in poblaciones_validas]
        
        #if self.poblacion not in poblacion_nombres:
          #  raise ValueError(f"La población seleccionada '{self.poblacion}' no es válida para la provincia '{self.provincia}'")
        
        super().save(*args, **kwargs)