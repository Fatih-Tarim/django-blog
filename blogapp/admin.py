from django.contrib import admin
from blogapp.models import ( 
    KategoriModel,
    YazilarModel,
    YorumModel,
    IletisimModel,
    UserDataModel
)

admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = (
        'baslik',
        'icerik'
    )
    list_display = (
        'baslik',
        'olusturma_tarihi', 
        'guncellenme_tarihi'
    )

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazar','olusturma_tarihi','guncellenme_tarihi')
    search_fields = ('yazar__username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email','isim_soyisim','mesaj','olusturma_tarihi')
    search_fields = ('email',)

@admin.register(UserDataModel)
class UserDataModelAdmin(admin.ModelAdmin):
    list_display = ('gender','age','estimated_salary')
    search_fields = ('purschased',)

