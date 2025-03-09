from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    numero = models.CharField(max_length=3)
    tipo   = models.CharField(max_length=15)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto  = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_ent = models.DateTimeField()
    data_sai = models.DateTimeField()

    def __str__(self):
            return f"{self.nome} - {self.cpf} em {self.data_ent}"


class Despesa(models.Model):
    desc_desp = models.CharField(max_length=30)
    valor_desp   = models.DecimalField(max_digits=10, decimal_places=2)
    data_desp    = models.DateTimeField()

    def __str__(self):
         return self.nome
    
class Receita(models.Model):
    desc_rec = models.CharField(max_length=30)
    valor_rec   = models.DecimalField(max_digits=10, decimal_places=2)
    data_rec    = models.DateTimeField()

    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

        

