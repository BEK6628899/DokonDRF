from rest_framework import serializers
from django.db.models import Sum,Avg,Max,Min
from .models import *


class BolimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'


class MahsulotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'
    def validation_chegirma(self,a):
        if a < 0 or a > 1000000:
            raise serializers.ValidationError("Chegirma narxi 0 va 1 milion oralig`ida bo`lishi kerak!")
        return a

    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        malumot['yangi_narx'] = instance.narx - instance.chegirma

        izohlar = Izoh.objects.filter(mahsulot=instance)
        malumot['ortacha_reyting'] = izohlar.aggregate(Avg('reyting'))['reyting__avg']
        return malumot






class IzohSerializers(serializers.ModelSerializer):
    def validate_reyting(self, a):
        if a < 0 or a >= 5:
            raise serializers.ValidationError("Reyting bal 1 va 5 oralig`ida bo`lishi kerak!")
        return a
    class Meta:
        model = Izoh
        fields = '__all__'




