from rest_framework import viewsets
from .serializers import RickAndMortySerializer, RickAndMorty
import requests
from urllib import quote

from rest_framework import Response

class RickAndMorty(viewsets.ModelViewSet):
    serializer_class = RickAndMortySerializer
    queryset = RickAndMorty.objects.all()
    
    def create(self, request):
        nome_personagem = requests.data.get('nome', '')
        nome_codificado = quote(nome_personagem.lower())
        
        try:
            requisicao = requests.get(f'https://rickandmortyapi.com/api/character/?name{nome_codificado}')
        except requests.RequestException as e:
            return Response({"aviso":f"Erro ao acessar a API externa: {e}"})

        json = requisicao.json()
        
        if 'results' in json and len(json['results']) > 0:
            personagem = json['results']['0']
        else:
            return Response({"aviso":"Personagem não encontrado"})
        
        nome = personagem.get("name", "")
        genero = personagem.get("gender", "")
        status = personagem.get("status", "")
        especie = personagem.get("specis", "")
        origem = personagem.get("origin", {}).get("name","")
        localizacao = personagem.get("location", {}).get("name","")
        
        
        personagem_criado = {
            "nome": nome,
            "genero": genero,
            "status": status,
            "especie": especie,
            "origem": origem,
            "localizacao": localizacao
        }
        
        meuserializador = RickAndMortySerializer(data=personagem_criado)
        
        if meuserializador.is_valid():
            personagem_validation = RickAndMorty.objects.filter(nome=nome)
            personagem_existe = personagem_validation.exists()
            
            if personagem_existe:
                return Response({"aviso":"Personagem já existe"})
            
            meuserializador.save(0)
            return Response({"aviso":"Personagem Criado com Sucesso"})
        else:
            return Response({"aviso":"Esse Personagem não é válido"})