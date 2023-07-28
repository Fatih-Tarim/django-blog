from rest_framework import serializers

from blogapp.models import YorumModel, YazilarModel, KategoriModel


class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = YorumModel
        fields = "__all__"

    #serializer içerisinde string karşılıklarını almak 
    def get_yazar(self, obj):
        yazar = obj.yazar  
        return str(yazar)

    def get_yazi(self,obj):
        yazi = obj.yazi
        return str(yazi)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['yazar'] = self.get_yazar(instance)
        data['yazi'] = self.get_yazi(instance)
        return data

class YazilarSerializer(serializers.ModelSerializer):
    resim = serializers.ImageField(read_only=False)
    yazar = serializers.StringRelatedField(read_only=False)

    class Meta:
        model = YazilarModel
        fields = "__all__"
    
    def perform_create(self, serializer):
        yazar = self.request.user
        serializer.save(yazar= yazar)
    

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = "__all__"


