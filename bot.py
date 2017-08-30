import os
import turitopwebscrapping as ws


EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
COMPANY = os.environ['COMPANY']

loginUrl='https://app.turitop.com/admin/login/es/'
urlData='https://app.turitop.com/admin/company/' + COMPANY + '/bookings/calendar'

loginData = {
    'user': EMAIL,
    'password': PASSWORD,
    'submit': 'login',
}

output= ws.weblogin(loginUrl,loginData,urlData)
print output
