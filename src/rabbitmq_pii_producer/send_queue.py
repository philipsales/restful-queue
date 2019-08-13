import sys
import json
import pika
import sys 

import logs.logging_conf, logging
logger = logging.getLogger("send_queue.py")

class SendQueue(object):

    EXCHANGE_TYPE = 'topic'
    EXCHANGE_NAME = 'amqp.topic.pii-requests'
    PUBLISHING_INTERVAL = 1

    def __init__(self, data, msg_type):

        self._data = data
        self._type = msg_type 

        logger.info('messeage_type')
        logger.info(msg_type)

        #_credentials = pika.PlainCredentials("RabbitMQAdmin", "RabbitAdm(1)n@AWH")
        _credentials = pika.PlainCredentials("guest", "guest")
        #_ip_address = '172.104.54.251'
        _ip_address = 'localhost'
        _exchange_name = 'amqp.topic.pii-requests'
        _exchange_type = 'topic'

        self._connection = None
        self._channel = None

        self._deliveries = None
        self._acked = None
        self._nacked = None
        self._message_number = None

        self._stopping = False

        #connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address,socket_timeout=15, credentials=_credentials))
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
        channel = connection.channel()

        channel.exchange_declare(exchange=_exchange_name,
                                exchange_type=_exchange_type,
                                durable=True,
                                auto_delete=False)

        #_routing_key = 'anonymous.info'
        _routing_key = self._type
        _message =  '{ "body" : ' + self._data + ', ' + ' "type" : "' + self._type + '" }'
        _body  = json.dumps(_message)

        channel.confirm_delivery()
        channel.basic_publish(exchange=_exchange_name,
                              routing_key=_routing_key,
                              body=_body,
                              properties=pika.BasicProperties(delivery_mode=2),
                              mandatory=True)
        logger.info('[*] sent. %r: %r' %(_routing_key, _message))

        connection.close()


if __name__ == '__main__':
    SendQueue('','')