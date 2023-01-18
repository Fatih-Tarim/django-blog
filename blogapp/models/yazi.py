from django.db import models
from autoslug import AutoSlugField
from blogapp.models import KategoriModel
from django.contrib.auth.models import User

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazilar')
    yazar = models.ForeignKey(User, related_name='yazar', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Yazi'
        verbose_name_plural='Yazilar'
        db_name = 'Yazi'