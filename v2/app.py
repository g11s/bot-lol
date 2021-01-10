from lcu_driver import Connector
from client import Client
from core import Core

connector = Connector()


@connector.ready
async def connect(connection):
    Core.start()
    print('BOT está preparado para ser usado.')


@connector.close
async def disconnect(_):
    print('O cliente foi fechado.')
    await connector.stop()


@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def action(connection, event):
    playerResponse = event.data["playerResponse"]
    Client.acceptMatch(playerResponse)


@connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def action(connection, event):
    Client.executeLastAction()

# starts the connector
connector.start()