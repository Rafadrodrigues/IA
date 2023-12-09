from django.contrib import admin
from .models import Estudante

# Register your models here.

class EstudanteAdmin(admin.ModelAdmin):
    readonly_fields = ["registro_criado", "registro_atualizado"]


admin.site.register(Estudante)