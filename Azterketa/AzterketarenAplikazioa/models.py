from django.utils import timezone
from django.db import models

# Create your models here.
class Mediku(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)

    def __str__(self):
        return f"Medikuaren izena {self.izena} da eta abizena {self.abizena}."
    
class Paziente(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    zita_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pazientearen izena {self.izena} da eta abizena {self.abizena} eta baita ere zita bat dauka {self.zita_data }."
