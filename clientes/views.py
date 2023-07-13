from django.shortcuts import render
from .models import Cliente, Veiculo
from .forms import VeiculoForm, ClienteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
   return render(request, "index.html", {})

def cadastro(request):
   if request.method == "GET":
      form_cli = ClienteForm()
      form_vei = VeiculoForm()
      return render(request, "cadastro.html", {'cliente': form_cli, 'veiculo': form_vei})

   if request.method =="POST":
      form_cli = ClienteForm(request.POST)
      form_vei = VeiculoForm(request.POST)

      if form_vei.is_valid() and form_cli.is_valid():
         a = form_vei.cleaned_data['placa']
         b = form_cli.cleaned_data['nome']
         print(a)

         form_cli.save()
         form_vei.save()
         vei_obj = Veiculo.objects.get(placa=a)
         cli_obj = Cliente.objects.get(nome=b)
         vei_obj.dono = cli_obj
         vei_obj.save()
         
         

         return HttpResponse("ok")
      else:
         print(form_vei.errors)
         print(form_cli.errors)
         
         return HttpResponse("bad")