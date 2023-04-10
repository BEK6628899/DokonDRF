from django.db import models
from Userapp.models import *


class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    narx = models.IntegerField()
    chegirma = models.IntegerField()
    brened = models.CharField(max_length=30)
    batafsil = models.CharField(max_length=50)
    rasm = models.URLField(null=True, blank=True)
    holat = models.CharField(max_length=10)
    mavjud = models.CharField(max_length=5)
    sotuvchi = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom


class Izoh(models.Model):
    matn = models.CharField(max_length=60)
    reyting = models.CharField(max_length=10)
    sana = models.DateField()
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    def __str__(self):
        return self.matn



