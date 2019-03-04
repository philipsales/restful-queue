import sys 
sys.path.append('..')

from datetime import datetime
from flask import make_response, abort
import json

import rabbit_mq_producer.send_queue as rabbitmq 

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
