#rest-framework
from rest_framework import generics
from rest_framework import mixins

#models
from blogapp.models import YorumModel, YazilarModel, KategoriModel


#serializers
from blogapp.api.serializers import YorumSerializer, YazilarSerializer, KategoriSerializer, PostFotoSerializer










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








