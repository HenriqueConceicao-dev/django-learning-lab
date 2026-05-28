from django.db import models

# orm permite trabalahr com classe e metodos do pthon

class Cliente(models.Model):
    QUEIXA_CHOICES = (('D','Depressao'), ('A', 'Ansiedade'))

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    queixa = models.CharField(max_length=1 , choices=QUEIXA_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nome