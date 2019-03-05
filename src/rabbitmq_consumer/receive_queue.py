#!/usr/bin/env python
import pika
import sys
import json
import time
import connection.couchbase_n1ql as n1ql
import configuration.base_conf

#_credentials = pika.PlainCredentials('RabbitMQAdmin', 'RabbitAdm(1)n@AWH')
_credentials = pika.PlainCredentials('guest', 'guest')
_ip_address = 'localhost'
#rabbitMQ server
#_ip_address = '172.104.54.251'
_exchange_name = 'couchbase_upsert'
_exchange_type = 'topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address,socket_timeout=15, credentials=_credentials))
#connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
channel = connection.channel()

channel.exchange_declare(exchange=_exchange_name,
                         exchange_type=_exchange_type)

result = channel.queue_declare(exclusive=True, durable=True)
queue_name = result.method.queue

binding_keys = ['*.info', 'warning']

for binding_key in binding_keys:
    channel.queue_bind(exchange=_exchange_name,
                        queue=queue_name,
                        routing_key=binding_key)

print(' [*] Waiting.')

def callback(ch, method, properties, body):
    print(" [x] routing_key: %r, body:%r" % (method.routing_key, body))
    time.sleep(2)
    
    n1ql.couchbase_get(body)
    ch.basic_qos(prefetch_count=1)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()