from socket import socket
from json import loads
from base64 import b64decode

def main_client():
    client = socket()
    client.connect(('172.20.10.2', 8001))

    in_data = bytes()
    data = client.recv(1024)

    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('./__pycache__/' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('img saved.')

# Study Case : Email SMTP
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main_txtmail():
    sender = 'abc@126.com'
    receivers = ['efg@126.com', 'hij@126.com']
    message = MIMEText('用Python发邮件.', 'plain', 'utf-8')
    message['From'] = Header('ryan', 'utf-8')
    message['To']= Header('sally', 'utf-8')
    message['Subject'] = Header('email title', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('send mail successs.')


# Study case : Mail with subfile
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib

def main_mail():
    message = MIMEMultipart()

    text_content = MIMEText('please check subfile ', 'plain', 'utf-8')
    message['Subject'] = Header('this month', 'utf-8')
    message.attach(text_content)

    with open('./003.py','rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=003.py'
        message.attach(txt)

    with open('./table.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)

    smtper = SMTP('smtp.126.com')

    sender = 'abc@126.com'
    receivers = ['efg@126.com']

    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()

    print('send success.')


# study case : send message
import urllib.parse
import http.client
import json

def main():
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'

    params = urllib.parse.urlencode({'account':'APIID', 'password':'APIKEY', 'content':'您的验证码是：654321。请不要把验证码泄露给其他人。'
    , 'mobile': phonenumber, 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == '__main__':
    main()