from django.db import models

class Jogador(models.Model):

    POSICOES = [
        ("GOL", "Goleiro"),
        ("ZAG", "Zagueiro"),
        ("MEI", "Meia"),
        ("ATA", "Atacante"),
    ]

    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    posicao = models.CharField(max_length=3, choices=POSICOES)
    clube = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()

    foto = models.ImageField(
        upload_to="jogadores/",
        blank=True,
        null=True
    )

    capitao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Titulo(models.Model):

    competicao = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
    ano = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.competicao} - {self.resultado}"

class Selecao(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    continente = models.CharField(max_length=50)
    federacao = models.CharField(max_length=100)
    tecnico = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    fundacao = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome