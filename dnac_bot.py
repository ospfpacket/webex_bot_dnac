#Import modules
import os
from webex_bot.webex_bot import WebexBot

#Import the class commands from seperate python files
from gethealth import GetHealth
from mac import ClientByMac
from ip import ClientByIp

#Import the webex bot access token that was generated when you built your bot
#over at developer.webex.com
from webex_access_token import WEBEX_BOT_ACCESS_TOKEN

#Set parameters for the bot.
bot = WebexBot(WEBEX_BOT_ACCESS_TOKEN, approved_users=[<List of users here>])

#Call in the commands for use with the bot
bot.add_command(GetHealth())
bot.add_command(ClientByMac())
bot.add_command(ClientByIp())


#Run the bot
bot.run()
