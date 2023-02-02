from django import forms

class IletisimForm(forms.Form):
    email = forms.EmailField(required=True, max_length=100, label='E-Posta') 
    isim_soyisim = forms.CharField(max_length=25, label='Ad Soyad')
    mesaj = forms.CharField(widget=forms.Textarea(), label='Mesajınız')