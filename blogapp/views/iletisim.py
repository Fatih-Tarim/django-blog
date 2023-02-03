from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogapp.forms import IletisimForm
from blogapp.models import IletisimModel

def iletisim(request):
    form = IletisimForm(initial={
        'email':'example@gmail.com'
    })
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            # iletisim = IletisimModel()
            # iletisim.email = form.cleaned_data['email']
            # iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            # iletisim.mesaj = form.cleaned_data['mesaj']
            # iletisim.save()
            form.save()
            return redirect('anasayfa')

    context = {
        'form' : form
    }
    return render(request, 'pages/iletisim.html', context=context)

