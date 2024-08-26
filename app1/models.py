from django.db import models

class RickAndMorty(models.Model):
    
    nome = models.CharField(
        'Nome do Personagem',
        max_length=255,
        blank=False
    )
    
    genero = models.CharField(
        'Gênero do Personagem',
        max_length=10,
    )
    
    status = models.CharField(
        'Vivo ou Morto',
        max_length=10,
        blank=True
    )
    
    especie = models.CharField(
        'Especie do Personagem',
        max_length=20
    )
    
    origem = models.CharField(
        'Origem do Personagem',
        max_length=60
    )
    
    localizacao = models.CharField(
        'Localização do Personagem',
        max_length=60,
        blank=True
    )

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'
        
    def __str__(self):
        return self.nome
    