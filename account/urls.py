from django.urls import path, include
from account.views import cikis, sifre_degistir, profil_guncelle, kayit, ProfileDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('cikis', cikis, name='cikis'),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit', kayit, name='kayit'),
    path('giris', auth_views.LoginView.as_view(
        template_name = 'pages/giris.html'
    ), name='giris'),
    path('kullanici/<str:username>', ProfileDetailView.as_view(), name='user'),
]
