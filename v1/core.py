from screen import Screen
from config import pathImages
from client import Client

banChampionText = ''
posBanChampion = 0
selectChampionText = ''
posSelectChampion = 0


class Core:
    
    @staticmethod
    def setup():
        global banChampionText, selectChampionText

        banChampionText = input("Insira os nomes dos campeões que deseja banir separados por vírgula (yasuo, katarina): ")
        selectChampionText = input(
            "Insira os nomes dos campeões que deseja selecionar separados por vírgula (yasuo, katarina): ")

        print("\nPronto, agora pode iniciar a partida!\n")

        print(f"Se precisar trocar o campeão que deseja banir, pressione CTRL + X")
        print(f"Se precisar trocar o campeão que deseja selecionar, pressione CTRL + S")
        print("Se precisar sair, pressione ESC\n")

    @staticmethod
    def changeBan():
        global banChampionText

        banChampionText = input(
            "Insira o nome do campeão que deseja banir: ")

        print("\nEntendido capitão!")
        print(f"Agora baniremos {banChampionText}")

    @staticmethod
    def changeSelect():
        global selectChampionText

        resetPos()

        selectChampionText = input(
            "Insira o nome do campeão que deseja selecionar: ")

        print("\nEntendido capitão!")
        print(f"Agora selecionaremos {selectChampionText}")

    @staticmethod
    def checkNeedAcceptMatch():
        coordinatesAcceptMatch = Screen.search_image_on_screen(
            image_to_search=pathImages + "AcceptMatch.png")

        if coordinatesAcceptMatch:
            Client.acceptMatch(coordinatesAcceptMatch)

    @staticmethod
    def checkNeedSelectChampion():
        coordinatesMessageDeclareChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "MessageDeclareChampion.png")

        if coordinatesMessageDeclareChampion:
            selectOrBanChampion(selectChampionText, "Declarei")

    @staticmethod
    def checkNeedBanChampion():
        coordinatesMessageBanChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "MessageBanChampion.png")

        if coordinatesMessageBanChampion:
            selectOrBanChampion(banChampionText, "Bani")

    @staticmethod
    def checkNeedChooseChampion():
        coordinatesMessageSelectChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "MessageChooseChampion.png")

        if coordinatesMessageSelectChampion:
            selectOrBanChampion(selectChampionText, "Selecionei")

    @staticmethod
    def exit():
        print("\nSaindo do programa BotLol")


def resetPos():
    global posSelectChampion, posBanChampion
    posSelectChampion = 0
    posBanChampion = 0


def getChampionInList(champions, message):
    listChampions = champions.split(',')

    if message == 'Bani':
        pos = posBanChampion
    else:
        pos = posSelectChampion

    if len(listChampions) - 1 >= pos:
        return listChampions[pos].strip()

    return False


def nextSelectOrBanChampion(message: str):
    global banChampionText, posBanChampion, selectChampionText, posSelectChampion

    if message == "Bani":
        banChampionText = input("Insira o nome do próximo campeão para ser banido: ")
        posBanChampion = 0
        return getChampionInList(banChampionText, message)
    else:
        selectChampionText = input(
            "Insira o nome do próximo campeão para ser selecionado: ")
        posSelectChampion = 0
        return getChampionInList(selectChampionText, message)


def sumAlreadyBanOrSelect(message: str):
    global posSelectChampion, posBanChampion

    if message == 'Bani':
        posBanChampion = posBanChampion + 1
    elif message == 'Selecionei':
        posSelectChampion = posSelectChampion + 1


def selectOrBanChampion(champions: str, message: str):
    champion = getChampionInList(champions, message)

    if not champion:
        champion = nextSelectOrBanChampion(message)

    # Se remover pesquisa e click
    # Se o campeao for banido ou selecionado
    # Não é feito a pesquisa

    Client.clickInputSearch()

    Client.writeInSearch(champion)

    sumAlreadyBanOrSelect(message)

    if Client.checkChampionIsBanned():
        print("Ops! Esse campeão já foi banido.")
        return

    if not Client.clickInChampion(champion):
        print("Ops! Você não possui esse campeão.")
        return

    if Client.checkChampionIsSelected():
        print("Ops! Esse campeão já foi selecionado.")
        return

    if message == "Bani":
        Client.banChampion()
    else:
        Client.selectChampion()

    Client.checkIfFinish(message)