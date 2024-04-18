from django.db import models
from datetime import datetime # função para pegar dia e hora atual

# Create your models here.
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [ # Usado para o campo choice
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null = False , blank= False)
    legenda = models.CharField(max_length=150, null = False , blank= False)
    categoria = models.CharField(max_length=100 , choices= OPCOES_CATEGORIA, default= '') # Faz o usuário ter que escolher entre as opções de categoria ao instanciar um novo objeto
    descricao = models.TextField(null = False , blank= False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank= True)
    publicada = models.BooleanField(default= False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank = False)

    def __str__(self):
        return self.nome