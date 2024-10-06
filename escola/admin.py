from django.contrib import admin
from . import models

@admin.register(models.Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular')
    list_per_page = 20
    search_fields = ('nome', 'cpf')
    list_display_links = ('id', 'nome')
    
@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)

@admin.register(models.Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id', 'estudante')
    search_fields = ('estudante__nome', 'curso__codigo')