import requests
import sys
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Evento:
	def __init__(self, game, date, time, people, status):
		self.date = date
		self.time = time
		self.game = game
		self.people = people
		self.status = status

def webscrap(html):
    dias = 0
    maxdias = 5
    soup = BeautifulSoup(html,'html.parser')

    tabla = soup.table

    events = soup.find_all('tr',class_='bookings-calendar-event')
    textcalendar = ''

    for event in events:
        esFecha = event.find('div',class_='bookings-history-date-event')
        esStatus = event.find('div',class_='offline-bookings-event-status')
        cleanstatus= esStatus.getText().strip('\n')
        status=cleanstatus.strip(' ')
        esHour=event.find('div',class_='offline-bookings-event-time-inner')
        hora=esHour.getText().strip('\n')
        esPeople=event.find('div',class_='offline-bookings-event-total-booked-seats opacity-lomed')

        esStatus.getText()

        if esPeople != None:
            people = esPeople.getText().strip('\n')
        else:
            people = ''

        if esFecha != None:
	    dias +=1
	    if dias == maxdias:
	        break
            date = esFecha.getText()
            textcalendar = textcalendar + '\n' + date + '\n'
        else:
            date = ''

        if 'Deshacer' in status:
            status = 'Bloqueado'
            peope = ''

        textcalendar = textcalendar + hora + ' ' + status + ' '  + people + '\n'

    return textcalendar

def weblogin(urlLogin,loginData,urlData):
    session = requests.session()
    r = session.post(urlLogin, data=loginData)
    cal=session.get(urlData)
    calendar=cal.text
    resultados = webscrap(calendar)
    r.close
    return resultados
