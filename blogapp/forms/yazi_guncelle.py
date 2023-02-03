from django import forms
from blogapp.models import YazilarModel

class YaziGuncelleFormModel(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('slug','yazar')

