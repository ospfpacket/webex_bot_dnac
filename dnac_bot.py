#Import modules
import os
from webex_bot.webex_bot import WebexBot

#Import the class commands from seperate python files
from gethealth import GetHealth
from getclientdetails import GetClientDetails

#Import the webex bot access token that was generated when you built your bot
#over at developer.webex.com
from webex_access_token import WEBEX_BOT_ACCESS_TOKEN

#Set parameters for the bot.
bot = WebexBot(WEBEX_BOT_ACCESS_TOKEN, approved_users=[<user email addresses here>])

#Call in the commands for use with the bot
bot.add_command(GetHealth())
bot.add_command(GetClientDetails())


#Run the bot
bot.run()
