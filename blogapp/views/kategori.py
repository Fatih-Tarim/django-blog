from django.shortcuts import render, get_object_or_404
from blogapp.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator

def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug = kategoriSlug)
    yazilar = kategori.yazilar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar,2)
    return render(request, 'pages/kategori.html', context={
        'yazilar' : paginator.get_page(sayfa),
        'kategori_isim': kategori.isim
    })

