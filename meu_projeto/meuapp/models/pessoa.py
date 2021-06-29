from django.db import models
from . import Departamento, Telefone


class Pessoa(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'),
                    ('F', 'Feminino')]

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50,
                                 null=True)
    idade = models.IntegerField(default=0)
    sexo = models.CharField(max_length=10,
                            choices=SEXO_CHOICES,
                            default='M')
    departamento = models.ForeignKey(Departamento,
                                     on_delete=models.SET_NULL,
                                     null=True)
    telefones = models.ManyToManyField(Telefone)
