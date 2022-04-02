import os, sys
import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from process_qualtrics import allocator


def logReporter():
    """ Every time the program runs, this sends an email so I can know precisely when things stop working."""
    message = MIMEMultipart("alternative")
    message["Subject"] = 'Run Report'
    message["From"] = 'bluequizinvolvement@gmail.com'
    message["To"] = 'bluequizinvolvement@gmail.com'
    textFile = getFile('log.txt')
    text = ''
    for line in textFile:
        text += line
    textFile.close()
    pPart = MIMEText(text, "plain")
    message.attach(pPart)

    # Sendoff!
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('bluequizinvolvement@gmail.com', 'wwjjcwvylkigvyli')
        server.sendmail('bluequizinvolvement@gmail.com', 'bluequizinvolvement@gmail.com', message.as_string())


if __name__ == "__main__":
    logReporter()
    os.remove('log.txt')