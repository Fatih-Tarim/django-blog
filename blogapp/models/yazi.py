from django.db import models
from autoslug import AutoSlugField
from blogapp.models import KategoriModel
from ckeditor.fields import RichTextField
from blogapp.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to='yazi_resimleri', blank=True, null=True)
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()

    slug = AutoSlugField(populate_from='baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazilar')
    yazar = models.ForeignKey('account.CustomUserModel', related_name='yazar', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Yazi'
        verbose_name_plural='Yazilar'
        db_table = 'Yazi'

    def __str__(self):
       return self.baslik