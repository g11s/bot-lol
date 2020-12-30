import time

import keyboard

from screen_manager import ScreenManager
from client import Client

from config import pathImages

def run():
    banChampionText = input("Insira o nome do campeão que deseja banir: ")
    selectChampionText = input(
        "Insira o nome do campeão que deseja selecionar: ")

    print("\nPronto, agora pode iniciar a partida!\n")

    print("Se precisar trocar o campeão que deseja banir, pressione CTRL + X")
    print("Se precisar trocar o campeão que deseja selecionar, pressione CTRL + S")
    print("Se precisar sair, pressione ESQ\n")

    while True:
        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("X"):
            banChampionText = input(
                "Insira o nome do campeão que deseja banir: ")
            print("\nEntendido capitão!")
            print(f"Agora baniremos {banChampionText}")

        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("S"):
            selectChampionText = input(
                "Insira o nome do campeão que deseja selecionar: ")
            print("\nEntendido capitão!")
            print(f"Agora selecionaremos {selectChampionText}")

        if keyboard.is_pressed("ESC"):
            print("\nSaindo do programa BotLol")
            break

        coordinatesAcceptMatch = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "AcceptMatch.png")

        if coordinatesAcceptMatch:
            Client.acceptMatch(coordinatesAcceptMatch)

        coordinatesMessageDeclareChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageDeclareChampion.png")

        coordinatesMessageBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageBanChampion.png")

        coordinatesMessageSelectChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageChooseChampion.png")

        if coordinatesMessageDeclareChampion:
            selectOrBanChampion(selectChampionText, "Declarei")

        if coordinatesMessageBanChampion:
            selectOrBanChampion(banChampionText, "Bani")

        if coordinatesMessageSelectChampion:
            selectOrBanChampion(selectChampionText, "Selecionei")


def selectOrBanChampion(champion: str, message: str):
    Client.findInputSearch()

    Client.writeInSearch(champion)

    Client.clickInChampion(champion)

    if message != "Bani":
        Client.selectChampion()
    else:
        Client.banChampion()

    Client.checkIfFinish(message)


run()
