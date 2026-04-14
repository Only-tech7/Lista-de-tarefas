#models.py define os campos da tabela do banco de dados, ou seja, a estrutura da tabela. Ele é responsável por criar a tabela no banco de dados e definir os tipos de dados para cada campo. O models.py é onde você define as classes que representam as tabelas do banco de dados e os campos dessas tabelas. Cada classe representa uma tabela e cada atributo da classe representa um campo da tabela. O Django usa essas classes para criar as tabelas no banco de dados e para manipular os dados dessas tabelas.
from django.db import models
# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titulo

