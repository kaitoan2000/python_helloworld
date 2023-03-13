#!/usr/bin/python
import sys,requests,hashlib,json,time

def addhost():
    now = time.ctime()
    url = "https://xxxx/monitoring/check_mk/webapi.py?action=add_host&_username=automation&_secret=myautomationsecret"
    try:
        r = requests.get(url=url, verify=False, timeout=10)
        if r.status_code==200:
	    if r.json()['errnum']==0:
                total = r.json()['total']
	        server_list = r.json()['msg']
	    else:
		print 'Error at ' + now
        else :
            print 'Error at ' + now
    except requests.exceptions.HTTPError, err:
        return 'API FAILED at ' + now + str(err)
    except requests.exceptions.RequestException as err:
        print 'OOps: Something Else: ' + str(err)
    except requests.exceptions.ConnectionError as errc:
        print 'Error Connecting: ' + str(errc)
    except requests.exceptions.Timeout:
        print 'Timeout Error: '  + str(errt)
    return server_list

def get_all_hosts():
    url = "https://xxxx/monitoring/check_mk/webapi.py?action=get_all_hosts&_username=username&_secret=secret&request_format=json&output_format=json"
    try:
        r = requests.get(url=url, verify=False, timeout=10)
        if r.status_code==200:
           print 'Error at ' + now
           result = r.json()
        else :
            print 'Error at ' + now
    except requests.exceptions.HTTPError, err:
        return 'API FAILED at ' + now + str(err)
    except requests.exceptions.RequestException as err:
        print 'OOps: Something Else: ' + str(err)
    except requests.exceptions.ConnectionError as errc:
        print 'Error Connecting: ' + str(errc)
    except requests.exceptions.Timeout:
        print 'Timeout Error: '  + str(errt)
    return result


if __name__ == '__main__':
    now = time.ctime()
    username="automation"
    secret="7378c621-f2cd-4903-84eb-d263fab8a687"
    print get_all_hosts()
    #addhost()

