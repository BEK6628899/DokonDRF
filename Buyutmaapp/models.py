from django.db import models
from Asosiy.models import *
from Userapp.models import *
from django.db.models import Sum


class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)


class Savat(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE,null=True)
    sana = models.DateField(auto_now_add=True,null=True,blank=True)

class SavatItem(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    yetkazish_kuni = models.PositiveSmallIntegerField(default=4)
    savat = models.ForeignKey(Savat,on_delete=models.CASCADE,related_name="itemlari")
    umumiy_summa = models.IntegerField(null=True,blank=True)
    yetkazish_puli = models.IntegerField(default=15000)
    def save(self, *args, **kwargs):
        narx = self.mahsulot.narx-self.mahsulot.chegirma
        self.umumiy_summa = (self.miqdor * narx)+self.yetkazish_puli
        super().save(*args, **kwargs)


class Buyurtma(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE,null=True)
    savat = models.ForeignKey(Savat,on_delete=models.CASCADE,null=True)
    holat = models.CharField(max_length=30,blank=True)
    sana = models.DateField(auto_now_add=True,null=True)
    summa = models.IntegerField(null=True)
    def save(self, *args, **kwargs):
        itemlar=self.savat.itemlari.all()
        self.summa=itemlar.aggregate(summa=Sum('umumiy_summa')).get('summa')
        super().save(*args, **kwargs)




