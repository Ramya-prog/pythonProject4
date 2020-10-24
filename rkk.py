# -*- coding: utf-8 -*
import smtplib
email = 'ramyakeerthimr@gmail.com'
password = 'Ramyakeerthimr@1'
send_to_email = 'mallilinux@gmail.com'
message = 'This is my message'
try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    print(email)
    print(password)
    server_ssl.login(email, password)
    server_ssl.sendmail(email, send_to_email, message)
    server_ssl.close()
    print('email sent.')
except Exception as e:
    print('Something went wrong..{}', e)