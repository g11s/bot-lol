championNameToId = {
    "ANNIE": 1,
    "OLAF": 2,
    "GALIO": 3,
    "TWISTED FATE": 4,
    "XIN ZHAO": 5,
    "URGOT": 6,
    "LEBLANC": 7,
    "VLADIMIR": 8,
    "FIDDLESTICKS": 9,
    "KAYLE": 10,
    "MASTER YI": 11,
    "ALISTAR": 12,
    "RYZE": 13,
    "SION": 14,
    "SIVIR": 15,
    "SORAKA": 16,
    "TEEMO": 17,
    "TRISTANA": 18,
    "WARWICK": 19,
    "NUNU E WILLUMP": 20,
    "MISS FORTUNE": 21,
    "ASHE": 22,
    "TRYNDAMERE": 23,
    "JAX": 24,
    "MORGANA": 25,
    "ZILEAN": 26,
    "SINGED": 27,
    "EVELYNN": 28,
    "TWITCH": 29,
    "KARTHUS": 30,
    "CHO'GATH": 31,
    "AMUMU": 32,
    "RAMMUS": 33,
    "ANIVIA": 34,
    "SHACO": 35,
    "DR. MUNDO": 36,
    "SONA": 37,
    "KASSADIN": 38,
    "IRELIA": 39,
    "JANNA": 40,
    "GANGPLANK": 41,
    "CORKI": 42,
    "KARMA": 43,
    "TARIC": 44,
    "VEIGAR": 45,
    "TRUNDLE": 48,
    "SWAIN": 50,
    "CAITLYN": 51,
    "BLITZCRANK": 53,
    "MALPHITE": 54,
    "KATARINA": 55,
    "NOCTURNE": 56,
    "MAOKAI": 57,
    "RENEKTON": 58,
    "JARVAN IV": 59,
    "ELISE": 60,
    "ORIANNA": 61,
    "WUKONG": 62,
    "BRAND": 63,
    "LEE SIN": 64,
    "VAYNE": 67,
    "RUMBLE": 68,
    "CASSIOPEIA": 69,
    "SKARNER": 72,
    "HEIMERDINGER": 74,
    "NASUS": 75,
    "NIDALEE": 76,
    "UDYR": 77,
    "POPPY": 78,
    "GRAGAS": 79,
    "PANTHEON": 80,
    "EZREAL": 81,
    "MORDEKAISER": 82,
    "YORICK": 83,
    "AKALI": 84,
    "KENNEN": 85,
    "GAREN": 86,
    "LEONA": 89,
    "MALZAHAR": 90,
    "TALON": 91,
    "RIVEN": 92,
    "KOG'MAW": 96,
    "SHEN": 98,
    "LUX": 99,
    "XERATH": 101,
    "SHYVANA": 102,
    "AHRI": 103,
    "GRAVES": 104,
    "FIZZ": 105,
    "VOLIBEAR": 106,
    "RENGAR": 107,
    "VARUS": 110,
    "NAUTILUS": 111,
    "VIKTOR": 112,
    "SEJUANI": 113,
    "FIORA": 114,
    "ZIGGS": 115,
    "LULU": 117,
    "DRAVEN": 119,
    "HECARIM": 120,
    "KHA'ZIX": 121,
    "DARIUS": 122,
    "JAYCE": 126,
    "LISSANDRA": 127,
    "DIANA": 131,
    "QUINN": 133,
    "SYNDRA": 134,
    "AURELION SOL": 136,
    "KAYN": 141,
    "ZOE": 142,
    "ZYRA": 143,
    "KAI'SA": 145,
    "SERAPHINE": 147,
    "GNAR": 150,
    "ZAC": 154,
    "YASUO": 157,
    "VEL'KOZ": 161,
    "TALIYAH": 163,
    "CAMILLE": 164,
    "BRAUM": 201,
    "JHIN": 202,
    "KINDRED": 203,
    "JINX": 222,
    "TAHM KENCH": 223,
    "SENNA": 235,
    "LUCIAN": 236,
    "ZED": 238,
    "KLED": 240,
    "EKKO": 245,
    "QIYANA": 246,
    "VI": 254,
    "AATROX": 266,
    "NAMI": 267,
    "AZIR": 268,
    "YUUMI": 350,
    "THRESH": 412,
    "ILLAOI": 420,
    "REK'SAI": 421,
    "IVERN": 427,
    "BARDO": 432,
    "RAKAN": 497,
    "XAYAH": 498,
    "ORNN": 516,
    "SYLAS": 517,
    "WEEKO": 518,
    "APHELIOS": 523,
    "RELL": 526,
    "PYKE": 555,
    "YONE": 777,
    "SETT": 875,
    "LILLIA": 876
}

rolePositionToRole = {
    "RANDOM": "RANDOM",
    "JUNGLE": "JUNGLE",
    "BOTTOM": "ADC",
    "MIDDLE": "MID",
    "UTILITY": "SUP",
    "TOP": "TOP"
}


class Helpers:

    @staticmethod
    def convertNameToId(name):
        return championNameToId[name.strip()]

    @staticmethod
    def convertPositionToRole(position):
        return rolePositionToRole[position.upper()]

    @staticmethod
    def showAllChampions():
        print("1 - Aatrox, a Espada Darkin\n"
              "2 - Ahri, a Raposa de Nove Caudas\n"
              "3 - Akali, a Assassina Renegada\n"
              "4 - Alistar, o Minotauro\n"
              "5 - Amumu, a Múmia Triste\n"
              "6 - Anivia, a Criofênix\n"
              "7 - Annie, a Criança Sombria\n"
              "8 - Aphelios, a Arma dos Devotos\n"
              "9 - Ashe, a Arqueira do Gelo"
              "10 - Aurelion Sol, o Forjador de Estrelas\n"
              "11 - Azir, o Imperador das Areias\n"
              "12 - Bardo, o Protetor Andarilho\n"
              "13 - Blitzcrank, o Grande Golem a Vapor\n"
              "14 - Brand, a Vingança Flamejante\n"
              "15 - Braum, o Coração de Freljord\n"
              "16 - Caitlyn, a Xerife de Piltover\n"
              "17 - Camille, a Sombra de Aço\n"
              "18 - Cassiopeia, o Abraço da Serpente\n"
              "19 - Cho'Gath, o Terror do Vazio\n"
              "20 - Corki, o Bombardeiro Ousado\n"
              "21 - Darius, a Mão de Noxus\n"
              "22 - Diana, o Escárnio da Lua\n"
              "23 - Dr. Mundo, o Louco de Zaun\n"
              "24 - Draven, o Carrasco de Noxus\n"
              "25 - Ekko, o Rapaz que Estilhaçou o Tempo\n"
              "26 - Elise, a Aranha Rainha\n"
              "27 - Evelynn, o Abraço da Agonia\n"
              "28 - Ezreal, o Explorador Pródigo\n"
              "29 - Fiddlesticks, o Terror Ancestral\n"
              "30 - Fiora, a Grande Duelista\n"
              "31 - Fizz, o Trapaceiro das Marés\n"
              "32 - Galio, o Colosso\n"
              "33 - Gangplank, o Terror dos Doze Mares\n"
              "34 - Garen, o Poder de Demacia\n"
              "35 - Gnar, o Yordle Pré-Histórico\n"
              "36 - Gragas, o Badernista\n"
              "37 - Graves, o Foragido\n"
              "38 - Hecarim, a Sombra da Guerra\n"
              "39 - Heimerdinger, o Inventor Idolatrado\n"
              "40 - Illaoi, a Sacerdotisa Cráquem\n"
              "41 - Irelia, a Dançarina das Lâminas\n"
              "42 - Ivern, o Pai do Verde\n"
              "43 - Janna, a Fúria da Tormenta\n"
              "44 - Jarvan IV, o Exemplo de Demacia\n"
              "45 - Jax, o Grão-Mestre das Armas\n"
              "46 - Jayce, o Defensor do Amanhã\n"
              "47 - Jhin, o Virtuoso\n"
              "48 - Jinx, o Gatilho Desenfreado\n"
              "49 - Kai'Sa, a Filha do Vazio\n"
              "50 - Kalista, a Lança da Vingança\n"
              "51 - Karma, a Iluminada\n"
              "52 - Karthus, a Voz Mortal\n"
              "53 - Kassadin, o Andarilho do Vazio\n"
              "54 - Katarina, a Lâmina Sinistra\n"
              "55 - Kayle, a Justa\n"
              "56 - Kayn, o Ceifador das Sombras\n"
              "57 - Kennen, o Coração da Tempestade\n"
              "58 - Kha'Zix, o Ceifador do Vazio\n"
              "59 - Kindred, os Caçadores Eternos\n"
              "60 - Kled, o Cavaleiro Intratável\n"
              "61 - Kog'Maw, a Boca do Abismo\n"
              "62 - LeBlanc, a Farsante\n"
              "63 - Lee Sin, o Monge Cego\n"
              "64 - Leona, a Alvorada Radiante\n"
              "65 - Lillia, o Florir Receoso\n"
              "66 - Lissandra, a Bruxa Gélida\n"
              "67 - Lucian, o Purificador\n"
              "68 - Lulu, a Fada Feiticeira\n"
              "69 - Lux, a Dama da Luz\n"
              "70 - Malphite, o Fragmento do Monolito\n"
              "71 - Malzahar, o Profeta do Vazio\n"
              "72 - Maokai, o Ente Sinistro\n"
              "73 - Master Yi, o Espadachim Wuju\n"
              "74 - Miss Fortune, a Caçadora de Recompensas\n"
              "75 - Mordekaiser, o Revenã de Ferro\n"
              "76 - Morgana, a Caída\n"
              "77 - Nami, a Conjuradora das Marés\n"
              "78 - Nasus, o Curador das Areias\n"
              "79 - Nautilus, o Titã das Profundezas\n"
              "80 - Neeko, a Camaleoa Curiosa\n"
              "81 - Nidalee, a Caçadora Bestial\n"
              "82 - Nocturne, o Eterno Pesadelo\n"
              "83 - Nunu e Willump, o Garoto e seu Yeti\n"
              "84 - Olaf, o Berserker\n"
              "85 - Orianna, a Donzela Mecânica\n"
              "86 - Ornn, o Fogo sob a Montanha\n"
              "87 - Pantheon, a Lança Indestrutível\n"
              "88 - Poppy, a Guardiã do Martelo\n"
              "89 - Pyke, o Estripador das Águas Sangrentas\n"
              "90 - Qiyana, a Imperatriz dos Elementos\n"
              "91 - Quinn, as Asas de Demacia\n"
              "92 - Rakan, o Encantador\n"
              "93 - Rammus, o Tatu Blindado\n"
              "94 - Rek'Sai, a Escavadora do Vazio\n"
              "95 - Rell, a Dama do Ferro\n"
              "96 - Renekton, o Carniceiro das Areias\n"
              "97 - Rengar, o Acossador da Alcateia\n"
              "98 - Riven, a Exilada\n"
              "99 - Rumble, a Ameaça Mecânica\n"
              "100 - Ryze, o Mago Rúnico\n"
              "101 - Samira, a Rosa do Deserto\n"
              "102 - Sejuani, a Ira do Inverno\n"
              "103 - Senna, a Redentora\n"
              "104 - Seraphine, a Cantora Sonhadora\n"
              "105 - Sett, o Chefe\n"
              "106 - Shaco, o Bufão Demoníaco\n"
              "107 - Shen, o Olho do Crepúsculo\n"
              "108 - Shyvana, a Meio-Dragão\n"
              "109 - Singed, o Químico Louco\n"
              "110 - Sion, o Colosso Morto-Vivo\n"
              "111 - Sivir, a Mestra da Batalha\n"
              "112 - Skarner, a Vanguarda de Cristal\n"
              "113 - Sona, a Mestra das Cordas\n"
              "114 - Soraka, a Filha das Estrelas\n"
              "115 - Swain, o Mestre da Estratégia\n"
              "116 - Sylas, o Abjugado\n"
              "117 - Syndra, a Soberana Sombria\n"
              "118 - Tahm Kench, o Rei do Rio\n"
              "119 - Taliyah, a Tecelã de Pedras\n"
              "120 - Talon, a Sombra da Lâmina\n"
              "121 - Taric, o Escudo de Valoran\n"
              "122 - Teemo, o Explorador Veloz\n"
              "123 - Thresh, o Guardião das Correntes\n"
              "124 - Tristana, a Artilheira Yordle\n"
              "125 - Trundle, o Rei dos Trolls\n"
              "126 - Tryndamere, o Rei Bárbaro\n"
              "127 - Twisted Fate, o Mestre das Cartas\n"
              "128 - Twitch, o Semeador da Peste\n"
              "129 - Udyr, o Andarilho Espiritual\n"
              "130 - Urgot, o Encouraçado\n"
              "131 - Varus, a Flecha da Vingança\n"
              "132 - Vayne, a Caçadora Noturna\n"
              "133 - Veigar, o Pequeno Mestre do Mal\n"
              "134 - Vel'Koz, o Olho do Vazio\n"
              "135 - Vi, a Defensora de Piltover\n"
              "136 - Viktor, o Arauto das Máquinas\n"
              "137 - Vladimir, o Sanguinário Escarlate\n"
              "138 - Volibear, o Rugido do Trovão\n"
              "139 - Warwick, a Ira Descontrolada de Zaun\n"
              "140 - Wukong, o Macaco Rei\n"
              "141 - Xayah, a Rebelde\n"
              "142 - Xerath, o Mago Ascendente\n"
              "143 - Xin Zhao, o Senescal de Demacia\n"
              "144 - Yasuo, o Imperdoável\n"
              "145 - Yone, o Inesquecido\n"
              "146 - Yorick, o Pastor de Almas\n"
              "147 - Yuumi, a Gata Mágica\n"
              "148 - Zac, a Arma Secreta\n"
              "149 - Zed, o Mestre das Sombras\n"
              "150 - Ziggs, o Especialista em Hexplosivos\n"
              "151 - Zilean, o Guardião do Tempo\n"
              "152 - Zoe, o Aspecto do Crepúsculo\n"
              "153 - Zyra, a Ascensão dos Espinhos"
              )