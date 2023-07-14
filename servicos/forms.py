from django.forms import ModelForm
from django import forms
from .models import Servicos
        

class ServicosForm(ModelForm):
    aviso = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
        )
    escolha_servico = forms.Select(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
    class Meta:
        model = Servicos
        exclude = ['veiculos', 'data_inicio']
        


