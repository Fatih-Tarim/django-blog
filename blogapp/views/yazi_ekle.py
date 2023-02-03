from django.shortcuts import render, redirect
from blogapp.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m() #Save many to many 
        return redirect('detay', slug=yazi.slug)
    return render(request, 'pages/yazi_ekle.html', context={
        'form': form
    })