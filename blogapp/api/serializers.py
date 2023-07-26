from rest_framework import serializers

from blogapp.models import YorumModel, YazilarModel, KategoriModel


class YorumSerializer(serializers.ModelSerializer):
    # yazar = serializers.SerializerMethodField()
    # yazi = serializers.SerializerMethodField()
    class Meta:
        model = YorumModel
        fields = "__all__"

    # def get_yazar(self, obj):
    #     return f"{obj.yazar}"

    # def get_yazi(self,obj):
    #     return f"{obj.yazi}"
    
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
    resim = serializers.ImageField(read_only=True)
    kategoriler = serializers.StringRelatedField(many=True, read_only=True)
    yazar = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = YazilarModel
        fields = "__all__"

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = "__all__"


