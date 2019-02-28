import sys 
sys.path.append('..')

from datetime import datetime
from flask import make_response, abort
import json

import producer.send_queue as rabbitmq 

def create(item):
    _name = item.get("order_id", None)
    _type = "order"

    response = rabbitmq.SendQueue(json.dumps(item), _type)

    if _name:
        return make_response(
            "{name} successfully queued".format(name=_name), 201
        )
    else:
        abort(
            406,
            "Item name {lname} is null".format(name=_name),
        )
