
from django.urls import path
from blogapp.views import IletisimFormView, anasayfa, KategoriListView, yazilarim, DetayView, YaziEkleCreateView, YaziGuncelleUpdateView, YaziSilDeleteView, yorum_sil
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', IletisimFormView.as_view(), name='iletisim'),
    path('kategori/<slug:kategoriSlug>', KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yazi_ekle', YaziEkleCreateView.as_view(), name='yazi_ekle'),
    path('yazi_guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi_guncelle'),
    path('yazi_sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi_sil'),
    path('yorum_sil/<int:id>', yorum_sil, name='yorum_sil'),
    path("email-gonderildi/", TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ), name="email-gonderildi"),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),
    path('yonlendir', RedirectView.as_view(
        url = 'https://www.google.com'
    ), name='yonlendir'),
]
