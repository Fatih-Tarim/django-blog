from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogapp.forms import IletisimForm
from blogapp.models import IletisimModel
from django.views.generic import FormView


class IletisimFormView(FormView):
    template_name = 'pages/iletisim.html'
    form_class = IletisimForm
    success_url = ('iletisim/email-gonderildi')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def iletisim(request):
#     form = IletisimForm(initial={
#         'email':'example@gmail.com'
#     })
#     if request.method == 'POST':
#         form = IletisimForm(request.POST)
#         if form.is_valid():
#             # iletisim = IletisimModel()
#             # iletisim.email = form.cleaned_data['email']
#             # iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
#             # iletisim.mesaj = form.cleaned_data['mesaj']
#             # iletisim.save()
#             form.save()
#             return redirect('anasayfa')

#     context = {
#         'form' : form
#     }
#     return render(request, 'pages/iletisim.html', context=context)

