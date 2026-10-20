from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from vacinas.forms import VacinaForm
from vacinas.models import Vacina


# Create your views here.

# ==========================================
# VIEWS DE VACINAS
# ==========================================

class VacinaListView(ListView):
    model = Vacina
    template_name = 'vacinas/vacina_list.html'
    context_object_name = 'vacinas'


class VacinaDetailView(DetailView):
    model = Vacina
    template_name = 'vacinas/vacina_detail.html'
    context_object_name = 'vacina'


class VacinaCreateView(CreateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'vacinas/vacina_form.html'
    success_url = reverse_lazy('vacinas:vacinas')


class VacinaUpdateView(UpdateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'vacinas/vacina_form.html'
    success_url = reverse_lazy('vacinas:vacinas')


class VacinaDeleteView(DeleteView):
    model = Vacina
    template_name = 'vacinas/vacina_confirm_delete.html'
    success_url = reverse_lazy('vacinas:vacinas')

