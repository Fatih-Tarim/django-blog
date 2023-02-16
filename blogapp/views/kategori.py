from django.shortcuts import render, get_object_or_404
from blogapp.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class KategoriListView(ListView):
    template_name = 'pages/kategori.html'
    context_object_name = 'yazilar'
    paginate_by = 2

    def get_queryset(self):
        kategori = get_object_or_404(KategoriModel, slug=self.kwargs['kategoriSlug'])
        return kategori.yazilar.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(KategoriListView, self).get_context_data(**kwargs)
        self.kategori = get_object_or_404(KategoriModel, slug = self.kwargs['kategoriSlug'])
        context['kategori'] = self.kategori
        return context





# def kategori(request, kategoriSlug):
#     kategori = get_object_or_404(KategoriModel, slug = kategoriSlug)
#     yazilar = kategori.yazilar.order_by('-id')
#     sayfa = request.GET.get('sayfa')
#     paginator = Paginator(yazilar,2)
#     return render(request, 'pages/kategori.html', context={
#         'yazilar' : paginator.get_page(sayfa),
#         'kategori_isim': kategori.isim
#     })

