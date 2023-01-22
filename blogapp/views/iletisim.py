from django.shortcuts import render
from django.http import HttpResponse

def iletisim(request):
    context = {
        'key' : 'başlık içerik'
    }
    return render(request, 'pages/iletisim.html', context=context)

