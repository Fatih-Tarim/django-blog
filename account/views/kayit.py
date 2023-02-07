from django.shortcuts import render, redirect
from account.forms import KayitFormu
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login, authenticate


def kayit(request):
    if request.method == 'POST':
      form = KayitFormu(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        login(request,user)
        messages.success(request,'Kayıt İşlemi Başarılı!')
        return redirect('anasayfa')
    else:
        form = KayitFormu()
        

    return render(request, "pages/kayit.html",context={
        'form': form
    })