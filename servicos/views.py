from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
import urllib

from .models import Servicos
from clientes.models import Veiculo



def servicos(request):
  
  global placa_req

  if request.method == "GET":
    placa_req = request.GET.get('placa')

    #só vai para o serviço se estiver logado...
    if placa_req:
      try:
        cliente = get_object_or_404(Veiculo, placa=placa_req)
      except Veiculo.DoesNotExist:
        return HttpResponse("placa invalida")

      return render(request, "servicos/servico_Página-Inicial.html", {} )
    
    
    return render(request, "servicos/login.html", {})
     
  elif request.method == "POST": 
    veiculo = get_object_or_404(Veiculo, placa=placa_req)
    data = timezone.now()
    aviso = request.POST.get('aviso')
    escolha = request.POST.get('escolha_servico')

    servico = Servicos(escolha_servico=escolha, aviso=aviso, data_inicio=data, veiculo=veiculo)
    servico.save() 
     
    return redirect('servicos:confirmacao')
  
def confirmacao(request):
  if request.method == "GET":
    try:
      veiculo_cliente = Veiculo.objects.get(placa=placa_req)
      telefone_cliente = veiculo_cliente.dono.telefone
      nome_cliente = veiculo_cliente.dono.nome
      ultimo_servico = Servicos.objects.filter(veiculo=veiculo_cliente).latest('data_inicio')
      ultimo_aviso = ultimo_servico.aviso
      escolha = ultimo_servico.escolha_servico

      mensagem = enviar_msg(placa_req, nome_cliente, telefone_cliente, escolha, ultimo_aviso)
    
    except Veiculo.DoesNotExist and Servicos.DoesNotExist:
      return HttpResponse("BO")

    return render(request, "servicos/confirmacao_servico.html", {'zap': mensagem} )
  

def enviar_msg(placa, nome, telefone, servico, aviso):
  texto = f"-------\nplaca:{placa}.\nnome:{nome}.\ntelefone:{telefone}.\nservico:{servico}.\naviso:{aviso}.\n----------\n"  
  msg = urllib.parse.quote(texto)  
  mensagem_zap = f"https://wa.me/559992010132?text={msg}"
  
  return mensagem_zap
