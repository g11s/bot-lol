import time
import sys

from screen import Screen

from config import pathImages, pathChampionsImages


class Client:

    @staticmethod
    def acceptMatch(coordinate: int):
        Screen.click_on_screen(coordenate_to_click=coordinate)
        print("Aceitei a partida!")
        time.sleep(2)

    @staticmethod
    def clickInputSearch():
        coordinatesSearchChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "SearchChampion.png")

        Screen.click_on_screen(
            coordenate_to_click=coordinatesSearchChampion)
        time.sleep(2)

    @staticmethod
    def writeInSearch(champion: str):
        Screen.clear()
        time.sleep(0.5)

        Screen.write(champion)
        time.sleep(1)

    @staticmethod
    def checkChampionIsBanned():
        coordenateBanChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "banned.png")

        if coordenateBanChampion is None:
            return False

        return coordenateBanChampion

    @staticmethod
    def checkChampionIsSelected():
        coordenateSelectChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "selected.png")

        if coordenateSelectChampion is None:
            return False

        return coordenateSelectChampion

    @staticmethod
    def clickInChampion(champion: str):
        coordinateSelectChampion = Screen.search_image_on_screen(
            image_to_search=pathChampionsImages + champion + ".png")

        if coordinateSelectChampion is None:
            return False

        Screen.click_on_screen(
            coordenate_to_click=coordinateSelectChampion)

        time.sleep(2)

        return True

    @staticmethod
    def selectChampion():
        coordinateConfirmChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "ConfirmChampion.png")
        Screen.click_on_screen(
            coordenate_to_click=coordinateConfirmChampion)

        time.sleep(2)

    @staticmethod
    def banChampion():
        coordinateBanChampion = Screen.search_image_on_screen(
            image_to_search=pathImages + "BanChampion.png")
        Screen.click_on_screen(
            coordenate_to_click=coordinateBanChampion)

        time.sleep(2)

    @staticmethod
    def checkIfFinish(message: str):
        print(f"{message} personagem na partida!")

        if message == "Selecionei":
            print("\nO bot foi finalizado porque já realizou todas as ações!")
            print("Você pode abri-lo futuramente, na sua próxima partida.")
            print("Obrigado por utilizar :)")
            sys.exit()
