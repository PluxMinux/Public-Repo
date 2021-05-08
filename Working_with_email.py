import os
import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL, PASSWORD)

    subject = 'Python testing email.'
    body = 'testing 001'
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(SENDER, RECEIVER ,msg)