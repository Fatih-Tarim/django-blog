from django.urls import path, include

from blogapp.api.views import YorumViewSet, YazilarViewSet, KategoriViewSet

from rest_framework.routers import DefaultRouter

# yorum_list = YorumViewSet.as_view({'get':'list'})
# yorum_detay = YorumViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register('yorumlar', YorumViewSet, basename="yorumlar")
router.register('yazilar', YazilarViewSet, basename="yazilar")
router.register('kategoriler', KategoriViewSet, basename="kategoriler")

urlpatterns = [
     path('', include(router.urls)),
    # path("yorumlar", yorum_list, name="yorumlar"),
    # path("yorumlar/<int:pk>", yorum_detay, name="yorumlar")
]

