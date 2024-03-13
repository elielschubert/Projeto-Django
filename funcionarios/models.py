from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length = 100)
    edv = models.CharField(max_length = 8, unique = True)
    cargo = models.CharField(max_length = 100)
    setor = models.CharField(max_length = 100)
    endereco = models.TextField()
    horario_entrada = models.TimeField(blank=False)
    horario_saida = models.TimeField(blank=False)
    data_admissao = models.DateField(blank=False)
    
    def __str__(self):
        return self.nome

