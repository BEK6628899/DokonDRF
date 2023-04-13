from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']


class ProfilSerializers(serializers.Serializer):
    class Meta:
        model = Profil
        fields = '__all__'


class LoginUserSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()


