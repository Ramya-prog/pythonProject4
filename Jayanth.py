import smtplib

sender_email = "ramyakeerthimr@gmail.com"
rec_email = "mallilinux@gmail.com"
password = input(str("Please enter your password :"))
message = "Hi, the message was sent"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)