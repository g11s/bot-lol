from screen_manager import ScreenManager
from config import pathImages
from client import Client

banChampionText = ''
selectChampionText = ''


class Core:

    @staticmethod
    def setup():
        global banChampionText, selectChampionText

        banChampionText = input("Insira o nome do campeão que deseja banir: ")
        selectChampionText = input(
            "Insira o nome do campeão que deseja selecionar: ")

        print("\nPronto, agora pode iniciar a partida!\n")

        print("Se precisar trocar o campeão que deseja banir, pressione CTRL + X")
        print("Se precisar trocar o campeão que deseja selecionar, pressione CTRL + S")
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


def selectOrBanChampion(champion: str, message: str):
    Client.findInputSearch()

    Client.writeInSearch(champion)

    Client.clickInChampion(champion)

    if message == "Bani":
        Client.banChampion()
    else:
        Client.selectChampion()

    Client.checkIfFinish(message)