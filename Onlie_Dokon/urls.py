from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Asosiy/', include('Asosiy.url')),
    # path('Buyutmaapp/', include('Buyutmaapp.url')),
    path('Userapp/', include('Userapp.url')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



