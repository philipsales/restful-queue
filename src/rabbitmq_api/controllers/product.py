import sys 
sys.path.append('..')

from datetime import datetime
from flask import make_response, abort
import json

import rabbitmq_producer.send_queue as rabbitmq 
import logs.logging_conf, logging

logger = logging.getLogger("product.py")

def create(product):
    _name = product.get("name", None)
    _type = "product"

    rabbitmq.SendQueue(json.dumps(product), _type)

    if _name:
        return make_response(
            "{name} successfully queued".format(name=_name), 201
        )
    else:
        abort(
            406,
            "Product name {name} is null".format(name=_name),
        )
