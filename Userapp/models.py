from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    ism = models.CharField(max_length=40)
    rasm = models.URLField(blank=True,null=True)
    tel = models.CharField(max_length=15)
    tugilgan_yil = models.SmallIntegerField()
    jins = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism



