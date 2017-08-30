import requests
import sys
from bs4 import BeautifulSoup

def webscrap(html):
    soup = BeautifulSoup(html,'html.parser')

    tabla = soup.table

    events = soup.find_all('tr',class_='bookings-calendar-event')

    for event in events:
        esFecha = event.find('div',class_='bookings-history-date-event')
        esStatus=event.find('div',class_='offline-bookings-event-status')
        esHour=event.find('div',class_='offline-bookings-event-time-inner')
        esPeople=event.find('div',class_='offline-bookings-event-total-booked-seats opacity-lomed')

        esStatus.getText()

        if esPeople != None:
            people = esPeople.getText().strip('\n')
        else:
            people = ''
        if esFecha != None:
            date = esFecha.getText()
            print (  '\n' + date )
        else:
            date = ''
        textcalendar = esHour.getText().strip('\n') + ' ' + esStatus.getText().strip('\n') + ' '  + people

        return textcalendar

def weblogin(urlLogin,loginData,urlData):
    session = requests.session()
    r = session.post(urlLogin, data=loginData)
    cal=session.get(urlData)
    calendar=cal.text
    resultados = webscrap(calendar)

    return resultados
