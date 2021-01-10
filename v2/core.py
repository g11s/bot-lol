import time
import keyboard
import requests

from helpers import Helpers
from secret import Secret

authorization, port = Secret.getSecret()

fullUrl = "https://127.0.0.1:" + port

routeAllowed = ['TOP', 'MID', 'SUP', 'JUNGLE', 'ADC', 'RANDOM']
championRoutes: dict[str, dict[str, list[str]]] = {}
posBan = 0
posPick = 0


class Core:

    @staticmethod
    def start():
        welcome()

        while not keyboard.is_pressed("ctrl+q"):
            if keyboard.is_pressed("ctrl+b"):
                showChampions()

            if keyboard.is_pressed("ctrl+r"):
                configureRoles()

            if keyboard.is_pressed("ctrl+space"):
                showRoutes()

    @staticmethod
    def resetPosBan():
        global posBan

        posBan = 0

    @staticmethod
    def resetPosPick():
        global posPick

        posPick = 0

    @staticmethod
    def sumPos(typeAction):
        global posBan, posPick

        if typeAction == 'ban':
            posBan = posBan + 1
        elif typeAction == 'pick':
            posPick = posPick + 1

    @staticmethod
    def getPosBan():
        return posBan

    @staticmethod
    def getPosPick():
        return posPick

    @staticmethod
    def acceptMatch():
        time.sleep(1)
        r = requests.post(url="https://127.0.0.1:" + port + "/lol-matchmaking/v1/ready-check/accept",
                          headers={'Authorization': 'Basic ' + authorization, "Accept": "application/json"},
                          verify=False)

        if r.status_code == 204:
            print("Partida aceita!")

    @staticmethod
    def getStatusMatch():
        r = requests.get(url=fullUrl + "/lol-champ-select/v1/session",
                         headers={'Authorization': 'Basic ' + authorization, "Accept": "application/json"},
                         verify=False)

        if r.status_code == 200:
            return r.json()

        return False

    @staticmethod
    def getMyRoleAndCell(statusMatch):
        mySummonerID = getMe()

        me = list(filter(lambda user: user['summonerId'] == mySummonerID, statusMatch["myTeam"]))
        myRole = me[0]['assignedPosition']
        myCell = me[0]['cellId']

        if not myRole:
            return "RANDOM", myCell

        return Helpers.convertPositionToRole(myRole), myCell

    @staticmethod
    def getPhase(statusMatch):
        phase = statusMatch["timer"]["phase"]

        return phase

    @staticmethod
    def getLastAction(statusMatch, myActorCell):
        for action in statusMatch['actions']:
            for subAction in action:
                if subAction['actorCellId'] == myActorCell and subAction['isInProgress'] and not subAction['completed']:
                    return subAction

        return None

    @staticmethod
    def getPickIntent(statusMatch, myActorCell):
        for action in statusMatch['actions']:
            for subAction in action:
                if subAction['actorCellId'] == myActorCell and subAction['type'] == 'pick' and not subAction['completed']:
                    return subAction

        return None

    @staticmethod
    def getChampion(championId: str):
        r = requests.get(url=fullUrl + "/lol-champ-select/v1/grid-champions/" + championId,
                         headers={'Authorization': 'Basic ' + authorization, "Accept": "application/json"},
                         verify=False)

        if r.status_code == 200:
            return r.json()

        return False

    @staticmethod
    def ban(lastAction, champion, confirm=True):
        if not isBanned(champion) and executeAction(lastAction, champion, confirm):
            print("Bani campeão!")

        time.sleep(3)

    @staticmethod
    def pick(lastAction, champion, confirm=True):
        if not isSelected(champion) and executeAction(lastAction, champion, confirm):
            print("Selecionei campeão!")
            time.sleep(3)


def welcome():
    print("\nPressione CTRL+B para ver os campeões disponíveis para as rotas.")
    print("Pressione CTRL+R para configurar uma rota.")
    print("Pressione CTRL+SPACE para mostrar rotas configuradas.")
    print("Pressione CTRL+Q para iniciar BOT.\n")


def createRolePick(role):
    global championRoutes

    championSelect = input(
        "Quais campeões deseja JOGAR nesta rota separados por vírgula (Exemplo: yasuo, katarina): "
    )

    if role.upper() in championRoutes:
        bans = championRoutes[role.upper()]["ban"]
    else:
        bans = {}

    championRoutes[role.upper()] = dict(pick=championSelect.split(','), ban=bans)


def createRoleBan(role):
    global championRoutes

    championBan = input(
        "Quais campeões deseja BANIR nesta rota separados por vírgula (Exemplo: yasuo, katarina): "
    )

    if role.upper() in championRoutes:
        picks = championRoutes[role.upper()]["pick"]
    else:
        picks = {}

    championRoutes[role.upper()] = dict(pick=picks, ban=championBan.split(','))


def configureRoles():
    print("\nAs opções das rotas são (TOP, MID, SUP, JUNGLE, ADC ou RANDOM).")
    print("A rota RANDOM foi criada para jogar outros modos no LOL que não possuem rotas")
    role = input("Deseja configurar os campeões de qual rota: ")

    if role.upper() in routeAllowed:
        showAllChampions = input(
            "Deseja ver o nome dos campeões? Digite Y para sim ou N para não: "
        )

        if showAllChampions.upper() == "Y":
            showChampions()

        createRolePick(role)
        createRoleBan(role)

        print(f"\nRota {role.upper()} criada com sucesso.")
    else:
        print("\nRota inexistente.")

    time.sleep(1)

    welcome()


def showRoutes():
    if championRoutes == {}:
        print("Não foi criada nenhuma rota ainda")
    else:
        print(championRoutes)

    time.sleep(2)

    welcome()


def showChampions():
    Helpers.showAllChampions()

    time.sleep(2)

    welcome()


def isBanned(champion):
    championSelection = champion['selectionStatus']

    if not championSelection['isBanned'] and not championSelection['pickIntented'] and not championSelection['pickedByOtherOrBanned'] and not champion['disabled']:
        return False

    return True


def isSelected(champion):
    if not champion['disabled'] and champion['owned'] and (not champion['selectionStatus']['pickedByOtherOrBanned'] or champion['selectionStatus']['selectedByMe']):
        return False

    return True


def executeAction(lastAction, champion, confirm):
    if not lastAction['completed']:
        time.sleep(2)

        championId = champion['id']

        if confirm:
            data = {"championId": championId, "completed": "true"}
        else:
            data = {"championId": championId}

        r = requests.patch(url=fullUrl + "/lol-champ-select/v1/session/actions/" + str(lastAction['id']),
                           json=data,
                           headers={'Authorization': 'Basic ' + authorization, "Accept": "application/json"},
                           verify=False)

        if r.status_code == 204:
            return True

        return False


def getMe():
    r = requests.get(url=fullUrl + "/lol-chat/v1/me",
                     headers={'Authorization': 'Basic ' + authorization, "Accept": "application/json"},
                     verify=False)

    return r.json()['summonerId']