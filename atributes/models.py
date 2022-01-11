from django.db import models
from colorfield.fields import ColorField
# Create your models here.


class Collection(models.Model):
    annee = models.CharField(verbose_name ="Année", max_length=50)
    def __str__(self):
        return self.annee


class Taille(models.Model):
    name = models.CharField(verbose_name ="nom", max_length=50)

    def __str__(self):
        return self.name


class Pointure(models.Model):
    name = models.CharField(verbose_name ="nom", max_length=50)

    def __str__(self):
        return self.name
    
    
class Couleur(models.Model):
    name        = models.CharField(verbose_name ="nom", max_length=50)
    # hex_value   = models.CharField(max_length=7, verbose_name="Valeur hexadécimale")
    hex_value   = ColorField(max_length=7, verbose_name="Valeur hexadécimale")

    def __str__(self):
        return self.name