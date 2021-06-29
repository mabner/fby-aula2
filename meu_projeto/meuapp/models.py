# from django.db import models

# # No caso, o Telefone realmente pode ser de várias pessoas
# class Telefone(models.Model):
# 	ddd = models.IntegerField(default=0)
# 	numero = models.BigIntegerField(default=0)
# 	temWhatsapp = models.BooleanField()

# class Departamento(models.Model):
# 	nome = models.CharField(max_length=50)
# 	numero_sala = models.IntegerField(default=0)

# class Pessoa(models.Model):
# 	SEXO_CHOICES = [('M','Masculino'),
# 					('F','Feminino')]

# 	nome = models.CharField(max_length=50)
# 	sobrenome = models.CharField(max_length=50,
# 							null=True)
# 	idade = models.IntegerField(default=0)
# 	sexo = models.CharField(max_length=10,
# 			choices=SEXO_CHOICES,
# 			default='M')
# 	departamento = models.ForeignKey(Departamento,
# 							on_delete=models.SET_NULL,
# 							null=True)
# 	telefones = models.ManyToManyField(Telefone)
