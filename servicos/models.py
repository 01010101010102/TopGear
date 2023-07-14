from django.db import models
from clientes.models import Veiculo


class Servicos(models.Model):
    tipos_servicos = [
        ('LC', "lavagem_completa"),
        ('ML', "meia_lavagem"),
    ]

    escolha_servico = models.CharField(max_length=2, choices=tipos_servicos, db_column="escolha_servico", default="ML")
    aviso = models.CharField(max_length=60, db_column="aviso", null=True)
    data_inicio = models.DateField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "(%s, %s, %s)" % (self.escolha_servico, self.aviso, self.data_inicio)
    

#campo para msg de cliente. Ex: fulano vai buscar...

    




