from django import forms
from blogapp.models import YorumModel


class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum',)