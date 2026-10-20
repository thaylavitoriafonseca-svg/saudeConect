from django import forms

from vacinas.models import Vacina


class VacinaForm(forms.ModelForm):

    class Meta:
        model = Vacina
        fields = [
            'nome',
            'fabricante',
            'lote',
            'tipo_dose',
            'descricao',
        ]