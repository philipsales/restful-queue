# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

from rest_api import emit_logs

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

def create(item):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    name = item.get("name", None)
    quantity = item.get("quantity", None)

    
    rpc = emit_logs.Foobar(name)

    # Does the person exist already?
    if name:
        return make_response(
            "{name} successfully queued".format(name=name), 201
        )
    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Item name {lname} is null".format(name=name),
        )
