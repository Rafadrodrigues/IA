from django.db import models

# Create your models here.
class Estudante(models.Model):

    nome = models.CharField(max_length=200)

    # def __str__(self) -> str:
    #     return self.nome