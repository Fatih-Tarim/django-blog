from django.urls import path, include

from blogapp.api.views import YorumViewSet, YazilarViewSet, KategoriViewSet

from rest_framework.routers import DefaultRouter

# yorum_list = YorumViewSet.as_view({'get':'list'})
# yorum_detay = YorumViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register('yorumlar', YorumViewSet)
router.register('yazilar', YazilarViewSet)
router.register('kategoriler', KategoriViewSet)

urlpatterns = [
     path('', include(router.urls)),
    # path("yorumlar", yorum_list, name="yorumlar"),
    # path("yorumlar/<int:pk>", yorum_detay, name="yorumlar")
]

