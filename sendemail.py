#!/usr/bin/python
"Sapmle Send email with attachment script"
__author__      = "Kaitoan2000@gmail.com"
__copyright__   = "Copyright 2017"

import time,datetime,sys,os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.charset import Charset, BASE64
from email.mime.nonmultipart import MIMENonMultipart
from email import charset
 
def logging(string):
    log_file = "/tmp/sendemail.log"
    string = str(datetime.datetime.now()) + "\t" + string
    logfile = open(log_file, "a+")
    logfile.write(string + "\n")
    logfile.close()
 
 
def sendmail(smtpHost, smtpPort, sender, recipient, subject, body):
    try:
        server = smtplib.SMTP(smtpHost, smtpPort)
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        attachment = MIMEMultipart('text', 'csv', charset='utf-8')
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        cs = Charset('utf-8')
        cs.body_encoding = BASE64
        fp = open(filename, 'rb')
        attachment.set_payload(fp.read(), charset=cs)
        fp.close()
        msg.attach(attachment)

        texttosend = msg.as_string()
        for to in recipient.split(","):
            logging("[Info] Sendmail: %s - %s - %s - %s - %s - %s" % (smtpHost,smtpPort,sender,recipient,subject,body))
            server.sendmail(sender, to, texttosend)
 
    except Exception, e:
        logging("[Error] " + str(e) )
        return str(e)

if __name__ == '__main__':
    date = str(datetime.datetime.now())
    subject = 'Mail with attachment'
    filename = sys.argv[1]
    text = 'Hi ,'+ '\n\n' + 'Email at ' + date + '\n\n' + '\n' + 'Thanks and best regards' + '\n' + 'An.'
    maillist = 'youremail'
    sendmail('SMTPHOST',SMTPPORT,'sender@gmail.com',maillist,subject,text)
