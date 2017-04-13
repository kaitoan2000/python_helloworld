#!/usr/bin/env python
import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='lab2:9092')

        for i in range(100):
            producer.send('test', b"\xc2%d" % i)
            time.sleep(1)


def main():
    threads = [
        Producer()
    ]

    for t in threads:
        t.start()

    time.sleep(100)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
