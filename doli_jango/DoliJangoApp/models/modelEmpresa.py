from django.db import models
from unidecode import unidecode
from django.utils import timezone
from ..utils import load_country_txt
import os

RUTA_PAISES = os.path.join(os.path.dirname(__file__), 'locale', 'paises.txt')
PAISES_CHOICES = load_country_txt(RUTA_PAISES)


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=5)
    poblacion = models.CharField(max_length=100)
    pais = models.CharField(max_length=10, choices=PAISES_CHOICES)
    
    
def save(self, *args, **kwargs):
   super().save(*args, **kwargs)