#Import modules to be used in this command
from webex_bot.models.command import Command
import requests
import json

class ClientByIp(Command):
    def __init__(self):
        super().__init__(
            command_keyword="ip",
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
        
        ip_addr = message

        url = "https://<DNAC URL:PORT>/api/v1/host?hostIp=" + ip_addr

        payload={}
        headers = {
        'x-auth-token': token
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)     #Always verify your SSL connection in production
        #print(response.status_code)     #This is good to enable when troubleshooting in console
        response = json.loads(response.text)     #Response is a List of Dict
        response = response.get('response')      #Pull in the KVPair you want to work with
        if len(response) > 0:
            response = response[0]               #Convert to a straight dictionary for ease of data extraction
        else:
            return ("Host is not found.")

        if response['hostType'] == 'Wired':
            hostIp = response['hostIp']
            hostMac = response['hostMac']
            networkDevice = response['connectedNetworkDeviceName']
            interface = response['connectedInterfaceName']
            return ("IP Address: " + hostIp + "\n"
                   "MAC Address: " + hostMac + "\n"
                   "Switch: " + networkDevice + "\n"
                   "Interface: " + interface
            )
        elif response['hostType'] == 'Wireless':
            hostIp = response['hostIp']
            hostMac = response['hostMac']
            apName = response['connectedAPName']
            wlanName = response['wlanNetworkName']
            return ("IP Address: " + hostIp + "\n"
                    "MAC Address: " + hostMac + "\n"
                    "Access Point: " + apName + "\n"
                    "SSID: " + wlanName
            )
