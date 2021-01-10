import os
import time

from helpers import Helpers
from core import Core, championRoutes, createRolePick, createRoleBan


class Client:

    @staticmethod
    def acceptMatch(playerResponse):
        if playerResponse == "None":
            Core.acceptMatch()
            Core.resetPosPick()
            Core.resetPosBan()

    @staticmethod
    def executeLastAction():
        statusMatch = Core.getStatusMatch()

        if statusMatch:
            role, cell = Core.getMyRoleAndCell(statusMatch)
            phase = Core.getPhase(statusMatch)

            if phase == "PLANNING":
                lastAction = Core.getPickIntent(statusMatch, cell)
            else:
                lastAction = Core.getLastAction(statusMatch, cell)

            if phase == "FINALIZATION":
                print("\n\nA partida vai começar, bom jogo!")
                time.sleep(30)
                os._exit(1)

            if not lastAction:
                return False

            typeAction = lastAction['type']

            champion = getChampion(typeAction, role)

            if not champion:
                return False

            if phase == "PLANNING":
                Core.pick(lastAction, champion, False)
            elif typeAction == 'ban':
                Core.ban(lastAction, champion)
                Core.sumPos(typeAction)
            elif typeAction == 'pick':
                Core.pick(lastAction, champion)
                Core.sumPos(typeAction)


def getChampion(typeAction, role):
    if role not in championRoutes:
        print(f"Você não configurou a rota {role}.")
        time.sleep(2)
        return False

    if typeAction == 'ban':
        pos = Core.getPosBan()
    elif typeAction == 'pick':
        pos = Core.getPosPick()

    if len(championRoutes[role][typeAction]) <= pos:
        if typeAction == 'ban':
            createRoleBan(role)
            Core.resetPosBan()
        elif typeAction == "pick":
            createRolePick(role)
            Core.resetPosPick()

        pos = 0

    championId = str(Helpers.convertNameToId(championRoutes[role][typeAction][pos].upper()))

    champion = Core.getChampion(championId)

    return champion
