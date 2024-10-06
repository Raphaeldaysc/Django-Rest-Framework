from . import models, serializers
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EstudantesViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = models.Estudante.objects.all()
    serializer_class = serializers.EstudantesSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #tem que seguir o padrão de nome, se não, não funciona
    queryset = models.Curso.objects.all()
    #tem que seguir o padrão de nome, se não, não funciona
    serializer_class = serializers.CursosSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Matricula.objects.all()
    serializer_class = serializers.MatriculaSerializer
    
class ListaMatriculaEstudante(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = models.Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = serializers.ListaMatriculaPorEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = models.Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = serializers.ListaMatriculaPorCursoSerializer
    
