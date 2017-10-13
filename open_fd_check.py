#! /usr/bin/python
import subprocess
import sys

def get_file_open():
    cmd = "cat /proc/sys/fs/file-nr"
    try:
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output = ret.stdout.read().strip('\n').split('\t')
        return output
    except Exception, ex:
        print ex

def check():
    output = get_file_open()
    open_fd = int(output[0]) - int(output[1])
    file_max = int(output[2])
    warn = file_max/100*75
    crit = file_max/100*90
    open_perc = open_fd*100/file_max
    warn_perc = warn*100/file_max
    crit_perc = crit*100/file_max
    text = str(open_fd) + "(" + str(open_perc) + "%)" + " of " + str(file_max) + " allowed file descriptors open"
    if (open_fd < warn):
        return "OK " + text
        sys.exit(0)
    if (open_fd > crit):
        return "CRITICAL " + text
        sys.exit(2)
    if (open > warn):
        return "WARNING " + text
        sys.exit(1)

if __name__ == '__main__':
    print check()

