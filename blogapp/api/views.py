#rest-framework
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated

#models
from blogapp.models import YorumModel, YazilarModel, KategoriModel


#serializers
from blogapp.api.serializers import YorumSerializer, YazilarSerializer, KategoriSerializer

#permissions
from blogapp.api.permissions import CommentOwnerOrReadOnly, IsSuperUser

class YorumViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.CreateModelMixin,
                GenericViewSet):
    
    queryset = YorumModel.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAuthenticated, CommentOwnerOrReadOnly]

class YazilarViewSet(ReadOnlyModelViewSet):
    queryset = YazilarModel.objects.all()
    serializer_class = YazilarSerializer
    permission_classes = [IsAuthenticated]


class KategoriViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      GenericViewSet
                      ):
    queryset = KategoriModel.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = "slug"








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








