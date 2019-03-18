#!/usr/bin/env python
import pika
import sys
import json
import time
import connection.couchbase_n1ql as n1ql

import logs.logging_conf, logging
logger = logging.getLogger("receive_queue.py")


_credentials = pika.PlainCredentials('RabbitMQAdmin', 'RabbitAdm(1)n@AWH')
_ip_address = 'localhost'
#_ip_address = '172.104.54.251'
#_ip_address = '172.104.171.229'
_exchange_name = 'amqp.topic.product-orders'
_exchange_type = 'topic'

#connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address,socket_timeout=15, credentials=_credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
channel = connection.channel()

channel.exchange_declare(exchange=_exchange_name, 
                         exchange_type=_exchange_type, 
                         passive=False,
                         durable=True,
                         auto_delete=False) 
#for dynamic queue_name
#result = channel.queue_declare(exclusive=True, durable=True)

#for static queue_name
result = channel.queue_declare(queue='opencart_events', durable=True)

queue_name = result.method.queue

binding_keys = ['order']

for binding_key in binding_keys:
    channel.queue_bind(exchange=_exchange_name,
                       queue=queue_name,
                       routing_key=binding_key)

def callback(ch, method, properties, body):
    logger.info("[x] routing_key: %r, body:%r" % (method.routing_key, body))
    #time.sleep(2)
    result = n1ql.couchbase_get(body)
    logger.info('---CALLBACK----')
    ch.basic_qos(prefetch_count=2)


channel.basic_consume(callback, queue=queue_name, no_ack=True) 

try:
    channel.start_consuming()
finally:
    connection.close()