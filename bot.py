import os
import turitopwebscrapping as ws
import telepot
import logging
from telepot import Bot

logger = logging.getLogger()
logger.setLevel(logging.INFO)


EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
COMPANY = os.environ['COMPANY']
TOKEN = os.environ['TOKEN']

loginUrl='https://app.turitop.com/admin/login/es/'
urlData='https://app.turitop.com/admin/company/' + COMPANY + '/bookings/calendar'

loginData = {
    'user': EMAIL,
    'password': PASSWORD,
    'submit': 'login',
}


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
       #content_type, chat_type, chat_id = telepot.glance2(msg)
       print('Normal Message:', content_type, chat_type, chat_id)
       flavor = telepot.flavor(msg)
       command = msg['text']
       if command == '/start':
           bot.sendMessage(chat_id, text='Hi! I am a Telegram Bot!!')
       elif command == '/help':
           bot.sendMessage(chat_id, text="I don't have any help commands yet!")
       elif command == '/settings':
           bot.sendMessage(chat_id, text="I cannot be configured via any settings yet. Check back soon!")
       elif command == '/reservas':
           bot.sendMessage(chat_id, text= "Dame unos segundos...")
           logger.info('Llamando a webscrapping')
           calendario = ws.weblogin(loginUrl,loginData,urlData)
           logger.info('Post llamada')
           bot.sendMessage(chat_id, text=calendario )
       else:
           bot.sendMessage(chat_id, text="No te entiendo. Por ahora solo entiendo '/reservas")
       return('Message sent')

   else:
       raise telepot.BadFlavor(msg)
