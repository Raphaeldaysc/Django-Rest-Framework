from django.db import models


class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)
    
    def __str__(self) -> str:
        return f"{self.nome}"


class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.TextField(blank=False, null=False)
    NIVEL_CHOICES = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, default='B')

    def __str__(self) -> str:
        return f"{self.codigo} - {self.descricao}"


class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    PERIODO_CHOICES = [('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')]
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, default='M', blank=False, null=False)
    
    def __str__(self) -> str:
        return f"{self.estudante} - {self.curso} - {self.periodo}"