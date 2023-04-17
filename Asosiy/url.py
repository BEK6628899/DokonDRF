from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/',BolimAPIView.as_view()),
    path('mahsulotlar/<int:pk>/',MahsulotAPIView.as_view()),
    path('izohlar/<int:pk>/',IzohAPIView.as_view()),
    path('izohdelete/<int:pk>/',IzohOchirAPI.as_view()),
]



