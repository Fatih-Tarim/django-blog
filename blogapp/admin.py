from django.contrib import admin
from blogapp.models import ( 
    KategoriModel,
    YazilarModel,
    YorumModel,
    IletisimModel
)

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = (
        'baslik',
        'icerik'
    )
    list_display = (
        'baslik',
        'tarih', 
        'duzenlenme_tarihi'
    )

admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazar','olusturma_tarihi','guncellenme_tarihi')
    search_fields = ('yazar__username',)

admin.site.register(YorumModel, YorumAdmin)

class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email','isim_soyisim','mesaj','olusturma_tarihi')
    search_fields = ('email',)

admin.site.register(IletisimModel, IletisimAdmin)