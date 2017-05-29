import sys
sys.path.append('THRIFT')

from scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
import time
import random
import string

socket = TSocket.TSocket(host="127.0.0.1", port=1463)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(trans=transport, strictRead=False, strictWrite=False)
client = scribe.Client(protocol)
transport.open()


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

category = 'nhanpt5'
while True:
    random_sleep = str(random.randint(1, 5))
    message = str(time.time()) + "\t" + id_generator() + "\t" + random_sleep + "\t" + str(random.choice('abcdefghij')) + "\t" + str(random.random()) + "\t" + id_generator() + "\t" + str(random.random()) + "\t" + str(random.random()) + "\t" + id_generator()
    log_entry = scribe.LogEntry(category, message)
    result = client.Log(messages=[log_entry])
    print result
    time.sleep(1)

#if result == 0:
#  print 'success'
