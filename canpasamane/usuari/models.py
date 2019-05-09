from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class UserManager(BaseUserManager):
    def crear_usuari(self,nom_user,email,contrasenya):
        if not email:
            raise ValueError("És necessaria una adreça electronica")

        elif not nom_user:
            raise ValueError("És necessari un nom d'usuari")

        user = self.model(email=self.normalize_email(email),nom_user=nom_user)

        user.set_pass(contrasenya)
        user.save(using=self._db)
        return user

    def crear_superusuari(self,nom_user,email,contrasenya):
        user = self.crear_usuari(email=email,nom_user=nom_user,contrasenya=contrasenya)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
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
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    telefon = models.CharField(verbose_name="numero de telefon de contacte", max_length=9 )
    nom_user = models.CharField(verbose_name="nom usuari", max_length=30)
    cognoms_user = models.CharField(verbose_name="nom usuari", max_length=60)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    pais = models.CharField(default="ESP",max_length=3, choices=COUNTRY)

    object = UserManager()

    USERNAME_FIELD = "nom_user"
    REQUIRED_FIELDS = ["email"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse("usuari:profile", kwargs={"nom_user": self.nom_user})

    @property
    def is_staff(self):
        return self.is_admin