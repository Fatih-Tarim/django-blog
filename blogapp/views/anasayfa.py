from django.shortcuts import render
from blogapp.models import YazilarModel

def anasayfa(request):
    yazilar = YazilarModel.objects.all()
    return render(request, 'pages/anasayfa.html', context={
        'yazilar' : yazilar
    })

