from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class TanlanganAPIView(APIView):
    def get(self,request):
        tanlangan = Tanlangan.objects.all()
        serializer = TanlanganSerializer(tanlangan,many=True)
        return Response(serializer.data)

class BuyurtmaAPIView(APIView):
    def get(self,request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavatAPIVew(APIView):
    def get(self,request):
        savat = Savat.objects.all()
        serializer = SavatSerializer(savat,many=True)
        return Response(serializer.data)


class SavatIteamAPIVew(APIView):
    def get(self,request):
        savat = Savat.objects.get(profil__user=request.user)
        savat_item = SavatItem.objects.get(savat_fl=savat)
        serializerr = SavatIteamSerializer(savat_item, many=True)
        return Response(serializerr.data)

