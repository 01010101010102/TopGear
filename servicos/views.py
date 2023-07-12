from django.shortcuts import render
from .forms import ServicosForm
from django.http import HttpResponse

def servicos(request):
   

   if request.method == "GET":
        form_servico = ServicosForm()
        return render(request, "app/escolha_servico.html", {'form_servico': form_servico,})
   
   elif request.method == "POST":
      form_servico = ServicosForm(request.POST)
      
      if form_servico.is_valid():
        a = form_servico.cleaned_data
        print(a)
        return HttpResponse(render(request, "app/confirmacao_servico.html", {}))
        
      else:
        print(request)
        return render(request, "app/servicos.html", {'form_servico': form_servico,})


