
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario


class CadastroForm(UserCreationForm):
    username = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    nome_completo = forms.CharField(
        label="Nome completo",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite seu nome completo",
            "autocomplete": "name",
        })
    )

    telefone = forms.CharField(
        label="Telefone",
        max_length=20,
        widget=forms.TelInput(attrs={
            "class": "form-control",
            "placeholder": "(00) 00000-0000",
            "autocomplete": "tel",
        })
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Digite seu e-mail",
            "autocomplete": "email",
        })
    )

    password1 = forms.CharField(
        label="Criar senha",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Crie uma senha",
            "autocomplete": "new-password",
        })
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Digite a senha novamente",
            "autocomplete": "new-password",
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if email:
            email = email.strip().lower()
            cleaned_data["email"] = email
            cleaned_data["username"] = email

            if User.objects.filter(email__iexact=email).exists():
                self.add_error(
                    "email",
                    "Este e-mail já está cadastrado."
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        nome = self.cleaned_data["nome_completo"].strip().split()

        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.first_name = nome[0]
        user.last_name = " ".join(nome[1:])

        if commit:
            user.save()
            PerfilUsuario.objects.create(
                usuario=user,
                telefone=self.cleaned_data["telefone"]
            )

        return user
