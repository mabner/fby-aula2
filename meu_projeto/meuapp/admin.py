from django.contrib import admin
from .models import Pessoa, Departamento, Telefone

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Departamento)
admin.site.register(Telefone)
