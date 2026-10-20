from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy

from .models import LocalVacinacao

# Create your views here.

def locais(request):
    locais = LocalVacinacao.objects.all()

    return render(request, 'locais/locais.html', {
        'locais': locais
    })