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

        url = "https://<DNAC URL HERE>/api/system/v1/auth/token"     #DNAC URL HERE

        payload = ""
        headers = {
            'Authorization': 'Basic64 Auth'     #Basic64 Auth here
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify = False)     #Verification should be on in a production environment

        response = json.loads(response.text)
        
        token = (response['Token'])
        
        url = "https://<DNAC URL:Port>/dna/intent/api/v1/network-health?startTime=&endTime="     #DNAC URL and Port

        headers = {
            'x-auth-token': token
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)     #Verification should be on in a production environment
        
        
        response = json.loads(response.text)
        GlobalHealth = str(response['latestHealthScore'])
        WLCHealth = response.get('healthDistirubution')
        WLCHealth = (str(WLCHealth[3]['healthScore']))

        
        return  ("Global Health: " + GlobalHealth + ".\n"
                 "WLC Health: " + WLCHealth
        )
       
