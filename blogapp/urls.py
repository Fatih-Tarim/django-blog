
from django.urls import path
from blogapp.views import iletisim, anasayfa, kategori, yazilarim, DetayView, yazi_ekle, yazi_guncelle, yazi_sil, yorum_sil
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yazi_ekle', yazi_ekle, name='yazi_ekle'),
    path('yazi_guncelle/<slug:slug>', yazi_guncelle, name='yazi_guncelle'),
    path('yazi_sil/<slug:slug>', yazi_sil, name='yazi_sil'),
    path('yorum_sil/<int:id>', yorum_sil, name='yorum_sil'),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),
    path('yonlendir', RedirectView.as_view(
        url = 'https://www.google.com'
    ), name='yonlendir'),
]
