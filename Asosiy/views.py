from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializers


class MahsulotViewSet(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers


class IzohViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializers


