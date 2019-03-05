import pika
import sys
import json

class SendQueue(object):

    def __init__(self, data, msg_type):

        self._data = data
        self._type = msg_type 

        _credentials = pika.PlainCredentials("RabbitMQAdmin", "RabbitAdm(1)n@AWH")
        _ip_address = '172.104.54.251'
        #_ip_address = 'localhost'
        _exchange_name = 'couchbase_upsert'
        _exchange_type = 'topic'

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address,socket_timeout=15, credentials=_credentials))
        #connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
        channel = connection.channel()

        channel.exchange_declare(exchange=_exchange_name,
                                exchange_type=_exchange_type)

        _routing_key = 'anonymous.info'
        _message =  '{ "body" : ' + self._data + ', ' + ' "type" : "' + self._type + '" }'
        _body  = json.dumps(_message)

        channel.basic_publish(exchange=_exchange_name,
                              routing_key=_routing_key,
                              body=_body)

        print(' [*] sent. %r: %r' %(_routing_key, _message))

        connection.close()