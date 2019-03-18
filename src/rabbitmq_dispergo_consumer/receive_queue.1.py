#!/usr/bin/env python
import pika
import sys
import json
import time
import logging
import connection.couchbase_n1ql as n1ql

import logs.logging_conf, logging
logger = logging.getLogger("receive_queue.py")


_credentials = pika.PlainCredentials('RabbitMQAdmin', 'RabbitAdm(1)n@AWH')
_ip_address = 'localhost'
#_ip_address = '172.104.54.251'
#_ip_address = '172.104.171.229'
_exchange_name = 'amqp.topic.product-orders'
_exchange_type = 'topic'


def callback(ch, method, properties, body):
    logger.info("[x] routing_key: %r, body:%r" % (method.routing_key, body))
    time.sleep(2)
    
    response = n1ql.couchbase_get(body)
    logger.info(response)

    ch.basic_qos(prefetch_count=1)


def consumer():
    #connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address,socket_timeout=15, credentials=_credentials))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
    channel = connection.channel()
    channel.exchange_declare(exchange=_exchange_name, exchange_type=_exchange_type, durable=True) 

    #for dynamic queue_name
    result = channel.queue_declare(durable=True, exclusive=True)

    #for dynamic queue_name
    #result = channel.queue_declare(queue='opencart_events_1', durable=True)

    queue_name = result.method.queue

    #binding_keys = ['*.info', 'warning']
    binding_keys = ['product']

    for binding_key in binding_keys:
        channel.queue_bind(exchange=_exchange_name,
                            queue=queue_name,
                            routing_key=binding_key)

    logger.info('[*] Waiting.')

    channel.basic_consume(callback, queue=queue_name, no_ack=True) 
    channel.start_consuming()

if __name__ == '__main__':
    logger.info('initialize receive_queue.py')
    consumer()
