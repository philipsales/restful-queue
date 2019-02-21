import pika
import sys

_ip_address = 'localhost'
_exchange_name = 'couchbase_upsert'
_exchange_type = 'topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
channel = connection.channel()

channel.exchange_declare(exchange=_exchange_name,
                         exchange_type=_exchange_type)

_routing_key = 'anonymous.info'
_message = 'hello world'

channel.basic_publish(exchange=_exchange_name,
                      routing_key=_routing_key,
                      body=_message)

print(' [*] sent. %r: %r' %(_routing_key, _message))

connection.close()