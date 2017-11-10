#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time
import datetime
import smtplib
import sys
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.header import Header
 
def logging(string):
    log_file = "/tmp/sendmail.log"
    string = str(datetime.datetime.now()) + "\t" + string
    logfile = open(log_file, "a+")
    logfile.write(string + "\n")
    logfile.close()
 
 
def sendmail(smtpHost, smtpPort, sender, recipient, subject, body):
    try:
        server = smtplib.SMTP(smtpHost, smtpPort)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "%s" % Header(subject, 'utf-8')
        msg['From'] = "\"%s\" <%s>" % (Header(sender[0], 'utf-8'), sender[1])
	for to in recipient:
	    msg['To'] = "\"%s\" <%s>" % (Header(to[0], 'utf-8'), to[1])
        msg.attach(MIMEText(body.encode('utf-8'), 'plain','utf-8'))
        text = msg.as_string()
        for mailto in recipient:
            server.sendmail("", mailto[1], text)
 
    except Exception, e:
        logging("[Error] " + str(e) )
        return str(e)
if __name__ == '__main__':
    date = str(datetime.datetime.now())
    subject = u"""Đây là email có unicode"""
    text = u"""Xin chào, bạn đã nhận được email từ tôi \t"""
    from_address = [u'Phạm', 'youremail@email.com']
    maillist = [[u'Nguyễn', 'kaito.an2000@gmail.com'],[u'Ngân', 'youremail@gmail.com']]
    sendmail('SMTP_SERVER',SMTP_PORT,from_address,maillist,subject,text)
