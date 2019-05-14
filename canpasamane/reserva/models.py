from django.db import models
from usuari.models import Usuari
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Reserva(models.Model):
    id_usuari = models.ForeignKey(
        Usuari, on_delete = models.CASCADE
    )
    data_reserva = ArrayField(models.DateField())
    tramit = models.BooleanField(default=False)
    validada = models.BooleanField(default=False)