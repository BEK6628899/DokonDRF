from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class ProfilAPIView(APIView):
    def get(self,request,pk):
        profil = Profil.objects.get(id=pk)
        serializer = ProfilSerializers(profil)
        return Response(serializer.data)


class UserCreateAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProfilCreateAPI(APIView):
    def post(self, request):
        serializer = ProfilSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.data['username'],
                password = serializer.data['password']
                         )
            if user is None:
                return Response({"xabar":"Bunaqa user yo'q"}, status=status.HTTP_400_BAD_REQUEST)
            login(request,user)
            return Response({"xabar":"Tizimga kirildi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class LogoutView(APIView):
    def get(self,request):
        logout(request)
        return Response({"xabar":"Foydalanuvchi tizimdan chiqarildi!"},status=status.HTTP_200_OK)
