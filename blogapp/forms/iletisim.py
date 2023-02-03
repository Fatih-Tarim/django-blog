from django import forms
from blogapp.models import IletisimModel

class IletisimForm(forms.ModelForm):
    
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email','mesaj')




    # email = forms.EmailField(required=True, max_length=100, label='E-Posta') 
    # isim_soyisim = forms.CharField(max_length=25, label='Ad Soyad')
    # mesaj = forms.CharField(widget=forms.Textarea(), label='Mesajınız')