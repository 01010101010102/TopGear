from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30, db_column="nome")
    telefone = models.PositiveIntegerField(max_length=14, db_column="telefone", null=True)
    
    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    
    tipos_veiculos = [
        ("CC", "CARRO"),
        ("CM", "CAMINHONETE"),
        ("M", "MOTO"),
    ]
    veiculo = models.CharField(max_length=3, default="CARRO", choices=tipos_veiculos, db_column="tipo_veiculo")
    placa = models.CharField(max_length=8, db_column="placa")
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    

    def __str__(self):
        return "(%s, %s)" % (self.placa, self.tipo_veiculo)
    
