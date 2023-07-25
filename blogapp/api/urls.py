from django.urls import path, include

from blogapp.api.views import YorumAPIView, KategoriAPIView, YazilarAPIView, YaziResimEkle, YazilarDetailAPIView

urlpatterns = [
    # path("yorumlar", YorumAPIView.as_view(), name="yorumlar"),  
    # path("yazilar", YazilarAPIView.as_view(), name="yazilar"),  
    # path("yazilar/<str:slug>", YazilarDetailAPIView.as_view(), name="yazilar-detay"),  
    # path("yazi-resim", YaziResimEkle.as_view(), name="yazi-resim"),  
    # path("kategoriler", KategoriAPIView.as_view(), name="kategoriler"),  
]
