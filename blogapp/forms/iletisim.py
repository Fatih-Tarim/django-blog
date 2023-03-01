from django import forms
from blogapp.models import IletisimModel
from django.core.mail import send_mail

class IletisimForm(forms.ModelForm):
    
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email','mesaj')

    def send_email(self, message):
        send_mail(
            subject = 'İletişim formundan mesaj var!',
            message= message,
            from_email='dev.fatihtarim@gmail.com',
            recipient_list=['dev.fatihtarim@gmail.com'],
            fail_silently=False
        )



    # email = forms.EmailField(required=True, max_length=100, label='E-Posta') 
    # isim_soyisim = forms.CharField(max_length=25, label='Ad Soyad')
    # mesaj = forms.CharField(widget=forms.Textarea(), label='Mesajınız')