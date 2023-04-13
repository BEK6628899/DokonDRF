from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/',BolimAPIView.as_view()),
    path('mahsulotlar/',MahsulotAPIView.as_view()),
    path('izohlar/',IzohAPIView.as_view()),
]