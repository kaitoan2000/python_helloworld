#!/usr/bin/env python
import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        #consumer = KafkaConsumer(bootstrap_servers='lab2:9092',
        #                         auto_offset_reset='earliest')
	consumer = KafkaConsumer(bootstrap_servers='localhost:9093')
        consumer.subscribe(['test'])

        for message in consumer:
            print (message)


def main():
    threads = [
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(100)

if __name__ == "__main__":
    #logging.basicConfig(
    #    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    #    level=logging.INFO
    #    )
    main()
