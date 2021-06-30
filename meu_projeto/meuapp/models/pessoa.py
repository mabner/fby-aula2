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


class PessoaManager(models.Manager):

    def obter_todas_pessoas(self):
        return self.all()

    def obter_familia(self):
        pessoas = self.filter(sobrenome="Leite")
        return pessoas

    def obter_masculino(self):
        masculino = self.filter(sexo="M")
        return masculino

    def obter_feminino(self):
        feminino = self.filter(sexo="F")
        return feminino

    def obter_maioridade(self):
        maiores = self.filter(idade__gte=18)
        # gte -> greater than or equal to
        return maiores

    def obter_primeiro_cadastro(self):
        primeiro = self.get(id=1)
        return primeiro

    def pessoas_m(self):
        pessoas_m = self.filter(nome__startswith="M")
        return pessoas_m
