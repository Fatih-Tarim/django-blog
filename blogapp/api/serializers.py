from rest_framework import serializers

from blogapp.models import YorumModel, YazilarModel, KategoriModel












########Deneme-1######33
# class YorumSerializer(serializers.ModelSerializer):
#     yazar = serializers.StringRelatedField(read_only=True)
#     yazi = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = YorumModel
#         fields = "__all__"

# class YazilarSerializer(serializers.ModelSerializer):
#     resim = serializers.ImageField(read_only=True)
#     kategoriler = serializers.StringRelatedField(many=True, read_only=True)
#     class Meta:
#         model = YazilarModel
#         fields = "__all__"

# class PostFotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = YazilarModel
#         fields = ("resim",)

# class KategoriSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KategoriModel
#         fields = "__all__"

