
from django.urls import path
from blogapp.views import iletisim, anasayfa

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim')
]
