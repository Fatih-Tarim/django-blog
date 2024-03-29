#rest-framework
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated

#models
from blogapp.models import YorumModel, YazilarModel, KategoriModel

#serializers
from blogapp.api.serializers import YorumSerializer, YazilarSerializer, KategoriSerializer

#permissions
from blogapp.api.permissions import CommentOwnerOrReadOnly, IsSuperUser, BlogOwnerOrReadOnly

#pagination
from blogapp.api.pagination import SmallPagination, MediumPagination, LargePagination

#filters
from rest_framework.filters import SearchFilter, OrderingFilter
from blogapp.api.filters import YorumFilter

class YorumViewSet(ModelViewSet): 
    queryset = YorumModel.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAuthenticated, CommentOwnerOrReadOnly]
    lookup_field = "yorum"
    pagination_class = MediumPagination
    filter_backends = [YorumFilter, SearchFilter]
    search_fields = ['yorum', 'yazar__username']

 

class YazilarViewSet(ModelViewSet):
    queryset = YazilarModel.objects.all().order_by("id")
    serializer_class = YazilarSerializer
    permission_classes = [IsAuthenticated, BlogOwnerOrReadOnly]
    lookup_field = "slug"
    pagination_class = LargePagination
    filter_backends = [SearchFilter]
    search_fields = ['baslik', 'yazar__username']

    def perform_create(self, serializer):
        yazar = self.request.user
        serializer.save(yazar=yazar)


class KategoriViewSet(ModelViewSet):
    queryset = KategoriModel.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = "slug"
    pagination_class = SmallPagination
    filter_backends = [SearchFilter]
    search_fields = ['isim']




# ###Generic Denemeler 
# class YorumAPIView(generics.ListCreateAPIView):
#     queryset = YorumModel.objects.all()
#     serializer_class = YorumSerializer
#     permission_classes = []

# class YazilarAPIView(generics.ListCreateAPIView): 
#     queryset = YazilarModel.objects.all()
#     serializer_class = YazilarSerializer
#     permission_classes = []

# class YazilarDetailAPIView(generics.RetrieveDestroyAPIView):
#     queryset = YazilarModel.objects.all()
#     serializer_class = YazilarSerializer
#     permission_classes = []
#     lookup_field = "slug"



# class YaziResimEkle(generics.ListCreateAPIView):
#     queryset = YazilarModel.objects.all()
#     serializer_class = PostFotoSerializer



# class KategoriAPIView(generics.ListAPIView):
#     queryset = KategoriModel.objects.all()
#     serializer_class = KategoriSerializer
#     permission_classes = []








