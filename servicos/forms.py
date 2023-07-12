from django.forms import ModelForm

from .models import Servicos


class ServicosForm(ModelForm):
    class Meta:
        model = Servicos
        exclude = ['veiculos']
        


