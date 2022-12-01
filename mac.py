#Import modules to be used in this command
from webex_bot.models.command import Command
import requests
import json

class ClientByMac(Command):
    def __init__(self):
        super().__init__(
            command_keyword="mac",
            help_message="Get client details from DNAC",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):

        url = "https://<DNAC URL>/api/system/v1/auth/token"

        payload = ""
        headers = {
            'Authorization': 'Basic64 Auth Here'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify = False)     #Always verify your SSL connection in production
        #print(response.status_code)     #This is good to enable when troubleshooting in console
        response = json.loads(response.text)
        
        token = (response['Token'])

        message = message.split(' ')

        if len(message) == 3:
            message = message[2]
        else:
            message = message[1]
        
        mac_addr = message

        url = "https://<DNAC URL:PORT>/dna/intent/api/v1/client-detail?timestamp=1669166580000&macAddress=" + mac_addr

        payload={}
        headers = {
            'x-auth-token': token,
            '__runsync': 'True'
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)     #Always verify your SSL connection in production
        #print(response.status_code)     #This is good to enable when troubleshooting in console
        response = json.loads(response.text)
        detail = response.get('detail')
        if len(detail) == 0:
            return ("Host not found in DNAC.")
        hostName = str(detail['hostName'])
        hostMac = str(detail['hostMac'])
        vlanId = str(detail['vlanId'])
        hostIpV4 = str(detail['hostIpV4'])
        ssid = str(detail['ssid'])
        port = str(detail['port'])
        connectedAP = str(detail['clientConnection'])
        healthScore = detail.get('healthScore')
        overallHealth = (str(healthScore[0]['score']))

        return ('Hostname: ' + hostName + "\n"
                'IP Address: ' + hostIpV4 + "\n"
                'MAC Address: ' + hostMac + "\n"
                'VLAN: ' + vlanId + "\n"
                'Connected AP/Switch: ' + connectedAP + "\n"
                'SSID: ' + ssid + "\n"
                'Switchport: ' + port + "\n"
                'Overall Health: ' + overallHealth
        )
