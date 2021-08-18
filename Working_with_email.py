import os
import smtplib
email = os.environ.get('USER_EMAIL')
passw = os.environ.get('USER_PASS')
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#with smtplib.SMTP('localhost',1025) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email, passw)
 

    subject = 'Python testing email.'
    body = 'testing 001'
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(email, 'aaaaalven@gmail.com' ,msg)

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(email, passw)
# subject = 'Python testing email.'
# body = 'testing 001'
# msg = f'Subject: {subject}\n\n{body}'
# server.sendmail('alven.toraja@gmail.com', 'aaaaalven@gmail.com' ,msg)