import time
import datetime
import smtplib
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def logging(string):
    log_file = "/tmp/sendmail.log"
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
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        for to in recipient.split(","):
            logging("[Info] Sendmail: %s - %s - %s - %s - %s - %s" % (smtpHost,smtpPort,sender,recipient,subject,body))
            server.sendmail(sender, to, text)

    except Exception, e:
        logging("[Error] " + str(e) )
        return str(e)

if __name__ == '__main__':
    text = str(sys.argv[1])
    subject = "Sample"
    maillist = "kaito.an2000@gmail.com" 
    sendmail('host',25,'sender@gmail.com',maillist,subject,text)
