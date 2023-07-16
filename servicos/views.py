from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse

from .models import Servicos
from clientes.models import Veiculo



def servicos(request):
  
  global placa_req

  if request.method == "GET":
    placa_req = request.GET.get('placa')

    if placa_req:
      try:
        cliente = get_object_or_404(Veiculo, placa=placa_req)
      except cliente.DoesNotExist:
        raise HttpResponse("placa invalida")
      
      

      return render(request, "servicos/servico_Página-Inicial.html" )
    
    
    return render(request, "servicos/login.html", {})
  
   
  if request.method == "POST":
    try:
      veiculo = get_object_or_404(Veiculo, placa=placa_req)
    except Veiculo.DoesNotExist:
        raise HttpResponse("placa invalida")
    
    
    data = timezone.now()
    aviso = request.POST.get('aviso')
    escolha = request.POST.get('escolha_servico')

    servico = Servicos(escolha_servico=escolha, aviso=aviso, data_inicio=data, veiculo=veiculo)
    servico.save()
    return redirect(reverse("clientes:index"))
    
def buscar_telefone_por_placa(placa_):
  try:
    veiculo_cliente = Veiculo.objects.get(placa=placa_)
    telefone_cliente = veiculo_cliente.dono.telefone
    
  except Veiculo.DoesNotExist:
    return HttpResponse("BO")
  
  mensagem = f"https://wa.me/{telefone_cliente}"
  return mensagem

