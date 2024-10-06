from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', views.EstudantesViewSet, basename='Estudantes')
router.register('cursos', views.CursoViewSet , basename='Cursos')   
router.register('matriculas', views.MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', views.ListaMatriculaEstudante.as_view(), name='matriculas_estudante'),
    path('cursos/<int:pk>/matriculas/', views.ListaMatriculaCurso.as_view(), name='matriculas_curso')
]
