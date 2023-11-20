from django.db import models

# Create your models here.
class Estudante(models.Model):

    nome = models.CharField(max_length=200)

    # Um tupla para diferenciar o tipo de formacao
    formacao = (
        ('E', 'Estudante'),
        ('F', 'Professor'),
    )

    formacao_academica = models.CharField(max_length=30,choices=formacao,default='E')
    #Considerando que a primeira insercao seja nulo ou branco
    email = models.EmailField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.nome