#! /usr/bin/python
import sys,requests,hashlib,json,time
import urllib3
urllib3.disable_warnings()

def send_messages(mess):
    timestamp = long(round(time.time() * 1000))
    data = { 'uid':uid,
             'message': mess}
    mac = hashlib.sha256(oaid+str(data)+str(timestamp)+secretkey).hexdigest()
    print mac
    json_msg = {
        'oaid': oaid,
        'data': data,
        'timestamp': timestamp,
        'mac': mac
    } 
    r = requests.post(url=url, data=json.dumps(json_msg),verify=False)
    #r = requests.post(url=url, data=json.dumps(json_msg))
    print(r.status_code, r.reason)
    return r.text

if __name__ == '__main__':
    mess = sys.argv[1]
    #uid = sys.argv[2]
    url = "https://openapi.zaloapp.com/oa/v1/sendmessage/text"
    oaid = "2066220378631905835"
    uid = "2511225505091094674"
    secretkey='75O77hTg1M5D14qs8S8J'
    print send_messages(mess)

