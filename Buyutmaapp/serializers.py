from rest_framework import serializers
from .models import *


class TanlanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlangan
        fields = '__all__'

class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = '__all__'

    # def to_representation(self, instance):
    #     malumot = super().to_representation(instance)
    #     narx = instance.narx - instance.chegirma
    #
    #     malumot["umumiy_narx"] = narx*instance.miqdor
    #
    #     return malumot
class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'


class SavatIteamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = '__all__'



