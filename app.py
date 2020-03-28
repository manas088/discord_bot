import discord
from constants import DISCCORD_BOT_TOKEN,BOT_NAME
from ext_api_call import get_bot_reply
token = DISCCORD_BOT_TOKEN
client = discord.Client()  # starts the discord client.
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger()

#  this method expected by  discord client. This runs once when connected to discord
@client.event
async def on_ready():
    logger.info(f'{client.user} client connection is ready with id ')

#this method will run when any message is received , and it will call get_bot_reply function.
@client.event
async def on_message(message):

    logger.info('Meggage from channel')
    logger.info(message.channel)
    logger.info(message.content)
    logger.info(message.author)
    users_message=message.content
    print(message.author.name)
    if message.author.name!=BOT_NAME:
        #get bot reply function which is called on the basis of message content
        message_to_reply = get_bot_reply(users_message,message.author.name)
        await message.channel.send(message_to_reply)


client.run(token)