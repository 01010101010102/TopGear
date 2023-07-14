from django.shortcuts import render, get_object_or_404
from .forms import ServicosForm
from django.http import HttpResponse
from .models import Servicos

def servicos(request):
  if request.method == "GET":
    placa_req = request.GET.get('placa')
    try:
      cliente = get_object_or_404(Servicos, placa=placa_req)
    except:
      raise HttpResponse("placa invalida")

    if cliente.exist():
      form_servico = ServicosForm()
      return render(request, "servicos/login.html", {'form_servico': form_servico})
   
  if request.method == "POST":
    form_servico = ServicosForm(request.POST)
    
    if form_servico.is_valid():
      a = form_servico.cleaned_data
      print(a)
      return HttpResponse(render(request, "app/confirmacao_servico.html", {}))
      
    else:
      print(request)
      return render(request, "app/servicos.html", {'form_servico': form_servico,})


