
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Cadastro realizado com sucesso! Faça login."
            )
            return redirect("login")
    else:
        form = CadastroForm()

    return render(
        request,
        "usuario/acesso/cadastro.html",
        {"form": form}
    )
