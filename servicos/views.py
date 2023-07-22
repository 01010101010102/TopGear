from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
import urllib

from .models import Servicos
from clientes.models import Veiculo



def servicos(request):
  
  global placa_req
  global whatsapp

  if request.method == "GET":
    placa_req = request.GET.get('placa')

    #só vai para o serviço se estiver logado...
    if placa_req:
      try:
        cliente = get_object_or_404(Veiculo, placa=placa_req)
      except Veiculo.DoesNotExist:
        raise HttpResponse("placa invalida")

      return render(request, "servicos/servico_Página-Inicial.html", {} )
    
    
    return render(request, "servicos/login.html", {})
  
   
  if request.method == "POST":
    try:
      veiculo = get_object_or_404(Veiculo, placa=placa_req)
    except Veiculo.DoesNotExist:
      return HttpResponse("placa invalida")
    
    
    data = timezone.now()
    aviso = request.POST.get('aviso')
    escolha = request.POST.get('escolha_servico')

    
    servico = Servicos(escolha_servico=escolha, aviso=aviso, data_inicio=data, veiculo=veiculo)
    servico.save()

    telefone_cliente, nome_cliente = buscar_telefoneNome_pela_placa(placa_req)
    enviar_msg(placa_req, nome_cliente, telefone_cliente, escolha, aviso)
    
    

    return render(request, "servicos/confirmacao_servico.html", {})
    
def confirmacao(request):
  
  return render(request, "confirmacao_servico.html", {})

def buscar_telefoneNome_pela_placa(placa_):
  try:
    veiculo_cliente = Veiculo.objects.get(placa=placa_)
    telefone_cliente = veiculo_cliente.dono.telefone
    nome_cliente = veiculo_cliente.dono.nome
    
  except Veiculo.DoesNotExist:
    return HttpResponse("BO")
  
  
  return telefone_cliente, nome_cliente

def enviar_msg(placa, nome, telefone, servico, aviso):
  texto = f"-------\nplaca:{placa}.\nnome:{nome}.\ntelefone:{telefone}.\nservico:{servico}.\naviso:{aviso}.\n----------\n"
  
  
  msg = urllib.parse.quote(texto)
  print(texto)
  print(msg)
  
  mensagem_zap = f"https://wa.me/559992010132?text={msg}"
  envio = urllib.request.urlopen(mensagem_zap)

  return envio
