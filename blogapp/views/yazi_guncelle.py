from django.shortcuts import render, redirect, get_object_or_404
from blogapp.forms import YaziGuncelleFormModel
from blogapp.models import YazilarModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziGuncelleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi_guncelle.html'
    fields = ('baslik', 'icerik', 'resim', 'kategoriler')

    def get_object(self):
        yazilar = get_object_or_404(
            YazilarModel,
            slug = self.kwargs.get('slug'),
            yazar = self.request.user
        )
        return yazilar
    
    def get_success_url(self):
        return reverse('detay', kwargs={
            'slug' : self.get_object().slug
        })



# @login_required(login_url='/')
# def yazi_guncelle(request, slug):
#     yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
#     form = YaziGuncelleFormModel(request.POST or None, files=request.FILES or None, instance=yazi)
#     if form.is_valid():
#         form.save()
#         redirect('detay', slug=yazi.slug)
#     return render(request, 'pages/yazi_guncelle.html', context={
#         'form': form
#     })