from django.urls import path
from .views import *

urlpatterns = [
    path('buyurtma/',BuyurtmaAPIView.as_view()),
    path('tanlangan/',TanlanganAPIView.as_view()),
    path('savat/',SavatAPIVew.as_view()),
    path('savatiteam/',SavatIteamAPIVew.as_view())
]
