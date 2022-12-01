#Import modules to be used in this command
from webex_bot.models.command import Command
import requests
import json

class GetHealth(Command):
    def __init__(self):
        super().__init__(
            command_keyword="gethealth",
            help_message="Get health stats from DNAC",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):
        #This splits the message into a list and selects the position to be passed for the mac_addr variable
        url = "https://<DNAC URL>/api/system/v1/auth/token"

        payload = ""
        headers = {
            'Authorization': 'Basic64 Auth Here'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify = False)     #Always verify your SSL connection in production

        #print(response.status_code)     #This is good to enable when troubleshooting status codes in the console

        response = json.loads(response.text)
        
        token = (response['Token'])
        
        url = "https://<DNAC URL:PORT>/dna/intent/api/v1/network-health?startTime=&endTime="

        headers = {
            'x-auth-token': token
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)     #Always verify your SSL connection in production
        
        
        response = json.loads(response.text)
        GlobalHealth = str(response['latestHealthScore'])
        WLCHealth = response.get('healthDistirubution')
        WLCHealth = (str(WLCHealth[3]['healthScore']))

        
        return  ("DNAC is reporting a Global Health Score of " + GlobalHealth + ".\n"
                 "DNAC is reporting a WLC Health Score of " + WLCHealth + "."
        )
