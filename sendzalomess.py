#! /usr/bin/python
import sys,requests,hashlib,json,time
import urllib3
urllib3.disable_warnings()

def send_messages(phoneno,msg):
    timestamp = long(round(time.time() * 1000))
    url = "https://openapi.zaloapp.com/oa/v1/sendmessage/text"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    uid = get_uid_by_phone(phoneno)
    data = { 'uid':uid,
             'message': msg}
    mac = hashlib.sha256(oaid+json.dumps(data)+str(timestamp)+secretkey).hexdigest()
    data = {
        'oaid': oaid,
        'data': json.dumps(data),
        'timestamp': timestamp,
        'mac': mac
    } 
    r = requests.post(url=url, data=data ,verify=False, headers=headers)
    if r.status_code==200:
	return 'OK'
    else :
	return 'FAILED'
    #print(r.status_code, r.reason)

def get_uid_by_phone(number):
   url = "https://openapi.zaloapp.com/oa/v1/getprofile"
   headers = {'content-type': 'application/x-www-form-urlencoded'}
   timestamp = long(round(time.time() * 1000))
   uid = number
   mac = hashlib.sha256(oaid+uid+str(timestamp)+secretkey).hexdigest()
   params = {
       'oaid': oaid,
       'uid': uid,
       'timestamp': timestamp,
       'mac': mac
   }
   r = requests.get(url=url, params=params, verify=False)
   return r.json()['data']['userId']

if __name__ == '__main__':
    oaid = "xxxx"        ##OA ZLPay.Alert
    secretkey='xxxx'    ##Secret Key fo OA
    phone = sys.argv[1]                 ##Phone number to send message
    msg = sys.argv[2]                   ##Message to send 
    phoneno = str("84") + str(phone[1:])
    print send_messages(phoneno,msg)
