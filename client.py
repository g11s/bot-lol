import win32gui
import time
import sys

from screen_manager import ScreenManager

from config import pathImages, pathChampionsImages, pathBanChampionsImages


class Client:

    @staticmethod
    def acceptMatch(coordinate: int):
        ScreenManager.click_on_screen(coordenate_to_click=coordinate)
        print("Aceitei a partida!")
        time.sleep(2)

    @staticmethod
    def findInputSearch():
        coordinatesSearchChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "SearchChampion.png")

        ScreenManager.click_on_screen(
            coordenate_to_click=coordinatesSearchChampion)
        time.sleep(2)

    @staticmethod
    def writeInSearch(champion: str):
        ScreenManager.clear()
        time.sleep(1)

        ScreenManager.write(champion)
        time.sleep(1)

    @staticmethod
    def checkChampionIsBan(champion: str):
        coordenateBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathBanChampionsImages + champion + ".png")

        return coordenateBanChampion

    @staticmethod
    def clickInChampion(champion: str):
        coordinateSelectChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathChampionsImages + champion + ".png")

        ScreenManager.click_on_screen(
            coordenate_to_click=coordinateSelectChampion)

        time.sleep(2)

    @staticmethod
    def selectChampion():
        coordinateConfirmChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "ConfirmChampion.png")
        ScreenManager.click_on_screen(
            coordenate_to_click=coordinateConfirmChampion)

        time.sleep(2)

    @staticmethod
    def banChampion():
        coordinateBanChampion = ScreenManager.search_image_on_screen(
            image_to_search=pathImages + "BanChampion.png")
        ScreenManager.click_on_screen(
            coordenate_to_click=coordinateBanChampion)

        time.sleep(2)

    @staticmethod
    def checkIfFinish(message: str):
        print(f"{message} personagem na partida!")

        if message == "Selecionei":
            print("\nO programa foi finalizado!")
            sys.exit()
