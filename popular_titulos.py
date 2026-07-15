from portal.models import Titulo

Titulo.objects.all().delete()

titulos = [

    {
        "competicao": "Jogos da Lusofonia",
        "resultado": "🥇 Medalha de Ouro",
        "ano": "2009"
    },

    {
        "competicao": "Jogos da Lusofonia",
        "resultado": "🥉 Medalha de Bronze",
        "ano": "2006"
    },

    {
        "competicao": "Taça Amílcar Cabral",
        "resultado": "🥈 Vice-campeão",
        "ano": "1991, 2007"
    },

    {
        "competicao": "Taça Amílcar Cabral",
        "resultado": "🥉 Terceiro Lugar",
        "ano": "1989, 1995"
    },

    {
        "competicao": "Taça Amílcar Cabral",
        "resultado": "4º Lugar",
        "ano": "1981, 1982, 1985"
    },

    {
        "competicao": "Jogos da CPLP",
        "resultado": "🥈 Medalha de Prata",
        "ano": "2010"
    },

    {
        "competicao": "Jogos da CPLP",
        "resultado": "🥉 Medalha de Bronze",
        "ano": "2014"
    },

    {
        "competicao": "Campeonato Africano das Nações",
        "resultado": "Quartas de Final",
        "ano": "2013, 2023"
    },

    {
        "competicao": "Campeonato Africano das Nações",
        "resultado": "Oitavas de Final",
        "ano": "2021"
    },

    {
        "competicao": "Campeonato Africano das Nações",
        "resultado": "Fase de Grupos",
        "ano": "2015"
    },

    {
        "competicao": "Copa do Mundo FIFA",
        "resultado": "Dezesseis avos de Final",
        "ano": "2026"
    },

]

for titulo in titulos:
    Titulo.objects.create(**titulo)

print(f"{len(titulos)} registros cadastrados!")