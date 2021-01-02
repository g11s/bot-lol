import keyboard
from core import Core


def start():
    Core.setup()

    while True:
        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("X"):
            Core.changeBan()

        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("S"):
            Core.changeSelect()

        if keyboard.is_pressed("ESC"):
            print("\nSaindo do programa BotLol")
            break

        Core.checkNeedAcceptMatch()

        Core.checkNeedSelectChampion()

        Core.checkNeedBanChampion()

        Core.checkNeedChooseChampion()


start()
