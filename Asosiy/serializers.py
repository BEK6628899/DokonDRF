from rest_framework import serializers
from .models import *


class BolimSerializers(serializers.Serializer):
    class Meta:
        model = Bolim
        fields = '__all__'


class MahsulotSerializers(serializers.Serializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'


class IzohSerializers(serializers.Serializer):
    class Meta:
        model = Izoh
        fields = '__all__'


