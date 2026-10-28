from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy

from .models import Vacina, Campanha, LocalVacinacao

# Create your views here.
# ==========================================
# VIEWS DE CAMPANHAS (TODAS AS ADICIONADAS AQUI)
# ==========================================

def campanhas(request):
    campanhas = Campanha.objects.all()

    return render(request, 'campanhas/campanhas.html', {
        'campanhas': campanhas
    })


class CampanhaCreateView(CreateView):
    model = Campanha
    fields = '__all__'
    template_name = 'campanhas/campanha_form.html'
    success_url = reverse_lazy('campanhas:campanhas')


class CampanhaDetailView(DetailView):
    model = Campanha
    template_name = 'campanhas/campanha_detail.html'
    context_object_name = 'campanha'


class CampanhaUpdateView(UpdateView):
    model = Campanha
    fields = '__all__'
    template_name = 'campanhas/campanha_form.html'
    success_url = reverse_lazy('campanhas:campanhas')


class CampanhaDeleteView(DeleteView):
    model = Campanha
    template_name = 'campanhas/campanha_confirm_delete.html'
    success_url = reverse_lazy('campanhas:campanhas')

