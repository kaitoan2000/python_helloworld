#!/usr/bin/env python
import sys
import check_mk_web_api

def get_all_hosts(): 
    return api.get_all_hosts()

def add_host(hostname, ip):
    api.add_host(hostname, ipaddress=ip)
    api.discover_services(hostname)
    return "Done"

def save(hostname, ip):
    api.discover_services(hostname)
    return "Done"

    
if __name__ == '__main__':
    username="automation"
    secret="7378c621-f2cd-4903-84eb-d263fab8a687"
    api = check_mk_web_api.WebApi('https://xxxx/monitoring/check_mk/webapi.py', username=username, secret=secret)    
    hostname = sys.argv[1]
    ip = sys.argv[2]
    print sys.argv[0] + " Hostname: " + hostname + " IP: " + ip
    add_host(hostname, ip)
    save(hostname, ip) 
    api.activate_changes()
    print get_all_hosts()
