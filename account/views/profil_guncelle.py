from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.forms import ProfilDuzenlemeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def profil_guncelle(request):
    
    if request.method == 'POST':
        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil güncelleme işlemi başarılı')
    else:
        form = ProfilDuzenlemeForm(instance = request.user)

    return render(request, "pages/profil-guncelle.html",context={
        'form' : form
    })