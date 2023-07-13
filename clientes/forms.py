from django.forms import ModelForm
from django import forms
from .models import Cliente, Veiculo

class ClienteForm(ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
        )
    telefone= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
        )
    class Meta:
        model = Cliente
        fields =['nome', 'telefone']       

class VeiculoForm(ModelForm):
    placa = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
        )
    veiculo = forms.Select(attrs={'class': 'u-border-none u-input u-input-rectangle u-palette-3-light-3 u-radius-10'})
    class Meta:
        model = Veiculo
        exclude = ['dono']
        
        