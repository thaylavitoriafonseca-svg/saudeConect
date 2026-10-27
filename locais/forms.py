from django import forms
from .models import LocalVacinacao


class LocalForm(forms.ModelForm):
    class Meta:
        model = LocalVacinacao
        fields = ['nome', 'endereco', 'cidade']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
        }