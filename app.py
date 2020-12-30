import os
import sys
import time

import keyboard

from screen_manager import ScreenManager

pathImages = os.path.dirname(os.path.realpath(__file__)) + "\images\\"
pathChampionsImages = pathImages + "champions\\"

def run():
    banChampionText = input("Insira o nome do campeão que deseja banir: ")
    selectChampionText = input("Insira o nome do campeão que deseja selecionar: ")

    print("\nPronto, agora pode iniciar a partida!\n")

    print("Se precisar trocar o campeão que deseja banir, pressione CTRL + D")
    print("Se precisar trocar o campeão que deseja selecionar, pressione CTRL + S")
    print("Se precisar sair, pressione ESQ\n")

    while True:
        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("D"):
            banChampionText = input("Insira o nome do campeão que deseja banir: ")
            print("\nEntendido capitão!")
            print(f"Agora baniremos {banChampionText}")

        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("S"):
            selectChampionText = input("Insira o nome do campeão que deseja selecionar: ")
            print("\nEntendido capitão!")
            print(f"Agora selecionaremos {selectChampionText}")

        if keyboard.is_pressed("ESC"):
            print("\nSaindo do programa BotLol")
            break

        coordinatesAcceptMatch = ScreenManager.search_image_on_screen(image_to_search=pathImages + "AcceptMatch.png")

        coordinatesMessageDeclareChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageDeclareChampion.png")

        coordinatesMessageBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageBanChampion.png")

        coordinatesMessageSelectChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "MessageChooseChampion.png")

        if coordinatesAcceptMatch:
            acceptMatch(coordinatesAcceptMatch)

        if coordinatesMessageDeclareChampion:
            selectOrBanChampion(selectChampionText, "Declarei")

        if coordinatesMessageBanChampion:
            selectOrBanChampion(banChampionText, "Bani")

        if coordinatesMessageSelectChampion:
            selectOrBanChampion(selectChampionText, "Selecionei")

def acceptMatch(coordinate: int):
    ScreenManager.click_on_screen(coordenate_to_click=coordinate)
    time.sleep(2)
    print("Aceitei a partida!")

def selectOrBanChampion(champion: str, message: str):
    coordinatesSearchChampion = ScreenManager.search_image_on_screen(image_to_search=pathImages + "SearchChampion.png")
    ScreenManager.click_on_screen(coordenate_to_click=coordinatesSearchChampion)
    time.sleep(2)

    ScreenManager.write(champion)
    time.sleep(3)

    coordinateSelectChampion = ScreenManager.search_image_on_screen(
        image_to_search=pathChampionsImages + champion + ".png")

    ScreenManager.click_on_screen(coordenate_to_click=coordinateSelectChampion)
    time.sleep(2)

    if message != "Bani":
        coordinateBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "ConfirmChampion.png")
        ScreenManager.click_on_screen(coordenate_to_click=coordinateBanChampion)
    else:
        coordinateConfirmChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "BanChampion.png")
        ScreenManager.click_on_screen(coordenate_to_click=coordinateConfirmChampion)

    time.sleep(2)

    print(f"{message} personagem na partida!")

    if message == "Selecionei":
        print("\nO programa foi finalizado!")
        sys.exit()

run()