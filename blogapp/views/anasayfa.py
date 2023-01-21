from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim':'Fatih'
    }
    return render(request, 'pages/anasayfa.html', context=context)

