import os
import base64
import urllib3

class Secret:

    @staticmethod
    def getSecret():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        command = "wmic process where \"caption=\'LeagueClientUx.exe\'\" get Caption,Processid,Commandline"

        try:
            key = os.popen(command).read().split("remoting-auth-token=")[1].split('"')[0]
            port = os.popen(command).read().split("app-port=")[2].split('"')[0]

            auth = "riot:"+key
            authByte = auth.encode('ascii')
            authBSFBytes = base64.b64encode(authByte)
            authorization = authBSFBytes.decode('ascii')
        except:
            print("Você precisa abrir o LOL e fazer login antes.")
            exit()

        return authorization, port
