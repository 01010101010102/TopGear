from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Servicos
from clientes.models import Veiculo


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
      
      
      return render(request, "servicos/servico_Página-Inicial.html",)
    
    
    return render(request, "servicos/login.html", {})
  
   
  if request.method == "POST":
    print(placa_req)
    print("-----------")
    try:
      veiculo = get_object_or_404(Veiculo, placa=placa_req)
    except veiculo.DoesNotExist:
        raise HttpResponse("placa invalida")
    
    """id_veic = veiculo.id
    print(id_veic)"""
    data = timezone.now()
    aviso = request.POST.get('aviso')
    escolha = request.POST.get('escolha_servico')

    

    
    servico = Servicos(escolha_servico=escolha, aviso=aviso, data_inicio=data, veiculo=veiculo)
    servico.save()
    return HttpResponse("ok")
    


