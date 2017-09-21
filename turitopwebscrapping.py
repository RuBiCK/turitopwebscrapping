import requests
import sys
import logging
from bs4 import BeautifulSoup
import turitop

logger = logging.getLogger()
logger.setLevel(logging.INFO)

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
COMPANY = os.environ['COMPANY']

loginUrl='https://app.turitop.com/admin/login/es/'
urlData = 'https://app.turitop.com/admin/company/' + COMPANY + '/calendar/monthly/' #Leter will add the service at the end of the URL

loginData = {
    'user': EMAIL,
    'password': PASSWORD,
    'submit': 'login',
}


def webscrapServices(html):
	soup = BeautifulSoup(html,'html.parser')
	tabla = soup.table
	events = soup.find_all('td',class_='offline-bookings-event-date-oneline')

def webscrap(html): #TODO cambiarlo por url
	dias = 0
	maxdias = 5
	soup = BeautifulSoup(html,'html.parser')

	tabla = soup.table

	events = soup.find_all('tr',class_='bookings-calendar-event')
	textcalendar = ''
	schedule = []

	for eventHtml in events:
		esFecha = eventHtml.find('div',class_='bookings-history-date-event')
		esStatus = eventHtml.find('div',class_='offline-bookings-event-status')
		cleanstatus= esStatus.getText().strip('\n')
		status=cleanstatus.strip(' ')
		esHour=eventHtml.find('div',class_='offline-bookings-event-time-inner')
		hora=esHour.getText().strip('\n')
		esPeople=eventHtml.find('div',class_='offline-bookings-event-total-booked-seats opacity-lomed')
		st = esStatus.getText()

		logger.info('event')
		schedule.append(event)

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
		event = Event(gameInvoked, esFecha, esHour, esPeople, st)
	logger.info(schedule)
    return textcalendar

def weblogin(urlLogin,loginData,urlData):
    session = requests.session()
    r = session.post(urlLogin, data=loginData)
    cal=session.get(urlData)
    calendar=cal.text
    resultados = webscrap(calendar)
    r.close
    return resultados

if __name__ == "__main__":
	turitopConn = weblogin(loginUrl + gameInvoked, loginData,urlData)
