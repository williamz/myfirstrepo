import requests
import time
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC55ffe46efc18a1499d3cddaea9f392e6"
auth_token  = "673068c68f1090557499ffb330709f38"
client = TwilioRestClient(account_sid, auth_token)
 
#message = client.messages.create(body="test msg",
#    to="+19059215665",
#    from_="+18678880388")
#print message.sid



Url = 'https://usvisa-info.com/en-CA/selfservice/p/reschedule_appointment'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
s = requests.Session()

s.headers.update(headers)

cookies = {'__utma': '1.622001591.1397695941.1397695941.1397695941.1',\
            '__utmb':'1.80.10.1397695941',\
            '__utmc':'1',\
            '__utmd':'1.1397695941.1.1',\
            '_appointment_system_session': '63754571570672e13c4414d7fa36bdcd'}

r = s.get(Url, cookies=cookies)
while True:
    time.sleep(30)
    r_old = r.text[10494:10515]
    r = s.get(Url, cookies=cookies)
    textMsg = 'The next available appointment date: *** ' + r.text[10494:10515] + ' ***'
    print ''
    print ''
    print time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print textMsg
    if r_old != r.text[10494:10515]:
        message = client.messages.create(body=r.text[10494:10515],
        to="+19059215665",
        from_="+18678880388")
        print message.sid

#print len(r.text)
#isWorking = r.text.find('The next available appointment')
#print isWorking




