import keyboard
from core import Core


def start():
    Core.setup()

    while True:
        if keyboard.is_pressed("ctrl+x"):
            Core.changeBan()

        if keyboard.is_pressed("ctrl+s"):
            Core.changeSelect()

        if keyboard.is_pressed("esc"):
            Core.exit()
            break

        Core.checkNeedAcceptMatch()

        Core.checkNeedSelectChampion()

        Core.checkNeedBanChampion()

        Core.checkNeedChooseChampion()


start()
