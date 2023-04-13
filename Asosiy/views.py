from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializers import *
from .models import *


class BolimAPIView(APIView):
    def get(self,request):
        bolim = Bolim.objects.all()
        serializer = BolimSerializers(bolim,many=True)
        return Response(serializer.data)
    def post(self,request):
        bolim = request.data
        serializer = BolimSerializers(data=bolim)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class MahsulotAPIView(APIView):
    def get(self,request):
        mahsulot = Mahsulot.objects.all()
        serializer = MahsulotSerializers(mahsulot,many=True)
        return Response(serializer.data)
    def post(self,request):
        mahsulot = request.data
        serializer = MahsulotSerializers(data=mahsulot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        soz = self.request.query_params.get('qidirish')   # /?qidirish=
        if soz is None or soz == "":
            natija = Mahsulot.objects.all()
        else:
            natija = Mahsulot.objects.filter(nom__contains=soz)
        return natija


class IzohAPIView(APIView):
    def get(self,request):
        izoh = Izoh.objects.all()
        serializer = IzohSerializers(izoh,many=True)
        return Response(serializer.data)
    def post(self,request):
        izoh = request.data
        serializer = IzohSerializers(data=izoh)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

