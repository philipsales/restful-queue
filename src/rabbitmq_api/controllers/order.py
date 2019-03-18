import sys 
sys.path.append('..')

from datetime import datetime
from flask import make_response, abort
import json
import rabbitmq_producer.send_queue as rabbitmq 

import logs.logging_conf, logging
logger = logging.getLogger("order.py")

def create(item):
    _name = item.get("order_id", None)
    _type = "order"

    rabbitmq.SendQueue(json.dumps(item), _type)

    if _name:
        return make_response(
            "{name} successfully queued".format(name=_name), 201
        )
    else:
        abort(
            406,
            "Item name {name} is null".format(name=_name),
        )
