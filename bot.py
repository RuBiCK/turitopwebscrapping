import os
import turitopwebscrapping as ws
import telepot
import logging
from telepot import Bot

logger = logging.getLogger()
logger.setLevel(logging.INFO)
gameInvoked=''

TOKEN = os.environ['TOKEN']
CHATSID = os.environ['CHATSIDS']





def telegramHandler(event, context):
	#print("Received event: " + json.dumps(event, indent=2))
	handle(event['message'])

def handle(msg):
    bot = Bot(TOKEN)
    # normal message
    if 1 == 1:
    #if flavor == 'normal':
		content_type, chat_type, chat_id = telepot.glance(msg)
		chat_id = msg['chat']['id']
        # only answer to a given list of authrized chats id
		if chat_id in CHATSID:
			#content_type, chat_type, chat_id = telepot.glance2(msg)
			print('Normal Message:', content_type, chat_type, chat_id)
			flavor = telepot.flavor(msg)
			command = msg['text']
			if command == '/reservas Goya':
				bot.sendMessage(chat_id, text="Dame unos segundos...")
				logger.info('Empezando webscrapping')
				# DELETE calendario = ws.weblogin(loginUrl + gameInvoked, loginData,urlData)
				logger.info('Finalizado Webscrapping')
				bot.sendMessage(chat_id, text=calendario )

			elif command == '/reservas Gotham':
				gameInvoked='P2'
				bot.sendMessage(chat_id, text= "A ver a ver... cuantos grupitos para Gotham tenemos :)")
				logger.info('Empezando webscrapping')
				calendario = ws.weblogin(loginUrl + gameInvoked, loginData,urlData)
				logger.info('Finalizado Webscrapping')
				bot.sendMessage(chat_id, text=calendario )


		else:
			bot.sendMessage(chat_id, text="Lo siento, parece que no estas autorizado para usar mis fantasticos servicios ;)")
			warningMessage='Attempt access from chatid: ' + chat_id
			logger.warning(warnigMessage)
		return('Message sent')
