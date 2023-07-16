from django.shortcuts import render, redirect
from .models import Cliente, Veiculo
from .forms import VeiculoForm, ClienteForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

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
         test_placa = Veiculo.objects.filter(placa=a)

         if test_placa.exists():
            return redirect(reverse("clientes:index")) 
         else:
         
            form_cli_instance = form_cli.save()  
            vei_obj = form_vei.save(commit=False)  

            vei_obj.dono = form_cli_instance  
            try:
               vei_obj.save()
            except:
               print("error-----------")
            return redirect("/clientes/")
      else:
         print(form_vei.errors)
         print(form_cli.errors)
         
         return HttpResponse("bad")