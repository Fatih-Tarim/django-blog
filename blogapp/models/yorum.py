from django.db import models
from django.contrib.auth.models import User
from blogapp.models import YazilarModel
from blogapp.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()

    class Meta:
        db_table='yorum'
        verbose_name='Yorum'
        verbose_name_plural='Yorumlar'

    def __str__(self) :
        return self.yazar.username