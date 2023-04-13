from django.urls import path
from .views import *

urlpatterns = [
    path('profil/<int:pk>/',ProfilAPIView.as_view()),
    path('create/',UserCreateAPI.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('logout/',LogoutView.as_view()),
]



