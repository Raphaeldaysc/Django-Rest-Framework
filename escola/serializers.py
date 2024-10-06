from rest_framework import serializers
from . import models

class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estudante
        fields = '__all__'
        
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = '__all__'
        
class ListaMatriculaPorEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = models.Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculaPorCursoSerializer(serializers.ModelSerializer):
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = models.Matricula
        fields = ['estudante', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()