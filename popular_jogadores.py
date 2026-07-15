from portal.models import Jogador

Jogador.objects.all().delete()

jogadores = [

    # GOLEIROS
    {"nome": "Vozinha", "numero": 1, "posicao": "GOL", "clube": "Chaves", "idade": 40},
    {"nome": "Márcio Rosa", "numero": 12, "posicao": "GOL", "clube": "Montana", "idade": 29},
    {"nome": "CJ dos Santos", "numero": 23, "posicao": "GOL", "clube": "San Diego Football Club", "idade": 25},

    # ZAGUEIROS
    {"nome": "Stopira", "numero": 2, "posicao": "ZAG", "clube": "Torreense", "idade": 38},
    {"nome": "Diney Borges", "numero": 3, "posicao": "ZAG", "clube": "Al Bataeh", "idade": 31},
    {"nome": "Roberto Lopes", "numero": 4, "posicao": "ZAG", "clube": "Shamrock Rovers", "idade": 34},
    {"nome": "Logan Costa", "numero": 5, "posicao": "ZAG", "clube": "Villarreal", "idade": 25},
    {"nome": "Sidny Lopes Cabral", "numero": 13, "posicao": "ZAG", "clube": "Benfica", "idade": 23},
    {"nome": "Steven Moreira", "numero": 22, "posicao": "ZAG", "clube": "Columbus Crew", "idade": 31},
    {"nome": "Wagner Pina", "numero": 24, "posicao": "ZAG", "clube": "Trabzonspor", "idade": 23},
    {"nome": "Kelvin Pires", "numero": 25, "posicao": "ZAG", "clube": "SJK", "idade": 26},

    # MEIAS
    {"nome": "Kevin Pina", "numero": 6, "posicao": "MEI", "clube": "FC Krasnodar", "idade": 29},
    {"nome": "João Paulo Fernandes", "numero": 8, "posicao": "MEI", "clube": "FCSB", "idade": 28},
    {"nome": "Jamiro Monteiro", "numero": 10, "posicao": "MEI", "clube": "Zwolle", "idade": 32},
    {"nome": "Garry Rodrigues", "numero": 11, "posicao": "MEI", "clube": "Apollon", "idade": 35},
    {"nome": "Deroy Duarte", "numero": 14, "posicao": "MEI", "clube": "Ludogorets Razgrad", "idade": 27},
    {"nome": "Laros Duarte", "numero": 15, "posicao": "MEI", "clube": "Puskás Akadémia", "idade": 29},
    {"nome": "Yannick Semedo", "numero": 16, "posicao": "MEI", "clube": "Farense", "idade": 30},
    {"nome": "Telmo Arcanjo", "numero": 18, "posicao": "MEI", "clube": "Vitória SC", "idade": 25},
    {"nome": "Nuno da Costa", "numero": 21, "posicao": "MEI", "clube": "İstanbul", "idade": 35},

    # ATACANTES
    {"nome": "Jovane Cabral", "numero": 7, "posicao": "ATA", "clube": "Estrela Amadora", "idade": 28},
    {"nome": "Gilson Tavares", "numero": 9, "posicao": "ATA", "clube": "FC Akron Togliatti", "idade": 24},
    {"nome": "Willy Semedo", "numero": 17, "posicao": "ATA", "clube": "Omonia", "idade": 32},
    {"nome": "Dailon Livramento", "numero": 19, "posicao": "ATA", "clube": "Verona", "idade": 25},
    {"nome": "Ryan Mendes", "numero": 20, "posicao": "ATA", "clube": "Iğdır FK", "idade": 36},
    {"nome": "Hélio Varela", "numero": 26, "posicao": "ATA", "clube": "Maccabi Tel-Aviv", "idade": 22},

]

for jogador in jogadores:
    Jogador.objects.create(**jogador)

print(f"{len(jogadores)} jogadores cadastrados com sucesso!")