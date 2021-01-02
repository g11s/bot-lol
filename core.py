from screen_manager import ScreenManager
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
        coordinatesAcceptMatch = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "AcceptMatch.png")

        if coordinatesAcceptMatch:
            Client.acceptMatch(coordinatesAcceptMatch)

    @staticmethod
    def checkNeedSelectChampion():
        coordinatesMessageDeclareChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageDeclareChampion.png")

        if coordinatesMessageDeclareChampion:
            selectOrBanChampion(selectChampionText, "Declarei")

    @staticmethod
    def checkNeedBanChampion():
        coordinatesMessageBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageBanChampion.png")

        if coordinatesMessageBanChampion:
            selectOrBanChampion(banChampionText, "Bani")

    @staticmethod
    def checkNeedChooseChampion():
        coordinatesMessageSelectChampion = ScreenManager.search_image_on_screen(
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
    else:
        selectChampionText = input(
            "Insira o nome do próximo campeão para ser selecionado: ")
        posSelectChampion = 0


def sumAlreadyBanOrSelect(message: str):
    global posSelectChampion, posBanChampion

    if message == 'Bani':
        posBanChampion = posBanChampion + 1
    else:
        posSelectChampion = posSelectChampion + 1


def selectOrBanChampion(champions: str, message: str):
    Client.findInputSearch()

    champion = getChampionInList(champions, message)

    if champion == False:
        nextSelectOrBanChampion(message)
        return

    Client.writeInSearch(champion)

    Client.clickInChampion(champion)

    sumAlreadyBanOrSelect(message)

    if Client.checkChampionIsBan(champion):
        print("Ops! Esse campeão já foi banido ou selecionado.")
        return

    if message == "Bani":
        Client.banChampion()
    else:
        Client.selectChampion()

    Client.checkIfFinish(message)