#!/usr/bin/python
## Check if all nodes redis cluster is in a correct status
## Usage: python check_redis_cluster.py [host] [port]
import subprocess
import sys
import os

def check(option):
    command = "/zserver/redis/bin/redis-cli -h %s -p %s info| grep %s" %(host, port, option)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output.split(':')[1].rstrip()

def main():
    role = check('role')

    if role == 'slave':
        # is asociated and read only?
        mls = check('master_link_status')
        sro = check('slave_read_only')
        master = check("master_host")
        if mls == 'up' and sro == '1':
            print "OK. Slave Redis read only and master (%s) redis is up" % master
            sys.exit(0)
        else:
            print "CRITICAL: Slave redis is not connected to master or not marked like read_only"
            sys.exit(2)
    elif role == 'master':
        # Check master status up
        slaves = check('connected_slaves')
        if slaves == "1":
            print "OK. Master redis (%s %s) and one slave connected." %(host,port)
            sys.exit(0)
        else:
            print "CRITICAL: Master redis (%s %s) with not slave connected" %(host,port)
            sys.exit(2)
    else:
        # Unexpected error, critical informing probably redis-cli not found
        print "CRITICAL: Redis cluster information is no correct (It's a cluster? redis-cli operative?)"
        sys.exit(2)

if __name__ == '__main__':
    #Input host, port
    host = str(sys.argv[1])
    port = str(sys.argv[2])
    main()
