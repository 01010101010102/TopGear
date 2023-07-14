from django.forms import ModelForm, TextInput, Select
from .models import Servicos
from django import forms

class ServicosForm(ModelForm):
    aviso = forms.CharField(widget=TextInput(attrs={'class': 'u-border-2 u-custom-font u-font-open-sans u-input u-input-rectangle u-radius-25 u-input-2'}))
    """escolha_servico = forms.Select(attrs={'class' : 'form-select',})"""
    
    
    """escolha_servico = forms.ChoiceField(widget=Select(attrs={'class': 'form-select', 'arial-label':'.form-select-lg example'}))"""
    
    class Meta:
        model = Servicos
        exclude = ['veiculos_serv', 'data_inicio']
