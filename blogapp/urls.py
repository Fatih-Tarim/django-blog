
from django.urls import path
from blogapp.views import iletisim, anasayfa

urlpatterns = [
    path('', anasayfa),
    path('iletisim', iletisim)
]
