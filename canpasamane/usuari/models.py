from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Usuari(models.Model):
    COUNTRY = (
        ("ESP", "Espana"),
        ("USA", "United States"),
        ("GB", "United Kingdom"),
        ("GER", "Deutschland"),
        ("NL", "Netherlands"),
        ("FR", "France"),
        ("BEL", "Belgium"),
        ("ITA", "Italia"),
    )
    usuari = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.IntegerField(verbose_name="numero de telefon de contacte")
    pais = models.CharField(default="ESP",max_length=3, choices=COUNTRY)
