from scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
import time
import random
import string
import thread

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def run(threadname):
    socket = TSocket.TSocket(host="127.0.0.1", port=1463)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(trans=transport, strictRead=False, strictWrite=False)
    client = scribe.Client(protocol)
    transport.open()
    category = 'test' + threadname
    print threadname
    while True:
        random_sleep = str(random.randint(1, 100))
        message = str(time.time()) + "\t" + id_generator() + "\t" + random_sleep + "\t" + str(
            random.choice('abcdefghij')) + "\t" + str(random.random()) + "\t" + id_generator() + "\t" + str(
            random.random()) + "\t" + str(random.random()) + "\t" + id_generator()
        log_entry = scribe.LogEntry(category, message)
        client.Log(messages=[log_entry])
        time.sleep(float(".0" + random_sleep))

if __name__ == "__main__":
    for i in range(0, 20):
        thread.start_new_thread(run, ("Thread" + str(i),))
    while True:
        pass
