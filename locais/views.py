from django.shortcuts import render, redirect, get_object_or_404
from .models import LocalVacinacao
from .forms import LocalForm


def listar_locais(request):
    locais = LocalVacinacao.objects.all()
    cidades = LocalVacinacao.objects.values_list(
        'cidade', flat=True
    ).distinct().order_by('cidade')

    return render(request, 'locais/locais.html', {
        'locais': locais,
        'cidades': cidades,
    })


def criar_local(request):
    form = LocalForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('locais:locais')

    return render(request, 'locais/locais_form.html', {
        'form': form,
    })


def detalhes_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)

    return render(request, 'locais/locais_detail.html', {
        'local': local,
    })


def editar_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)
    form = LocalForm(request.POST or None, instance=local)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('locais:detalhes_local', pk=local.pk)

    return render(request, 'locais/locais_form.html', {
        'form': form,
        'local': local,
    })


def excluir_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)

    if request.method == 'POST':
        local.delete()
        return redirect('locais:locais')

    return render(request, 'locais/locais_confirm_delete.html', {
        'local': local,
    })