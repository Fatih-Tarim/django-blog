
from django.urls import path
from blogapp.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yazi_ekle', yazi_ekle, name='yazi_ekle'),

]
