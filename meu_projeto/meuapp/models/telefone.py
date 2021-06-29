from django.db import models


class Telefone(models.Model):
    ddd = models.IntegerField(default=0)
    numero = models.BigIntegerField(default=0)
    temWhatsapp = models.BooleanField()
