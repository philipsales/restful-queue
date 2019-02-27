import sys 

from datetime import datetime
from flask import make_response, abort
import json

import connections.pmi_requests as pmi

def addPerson(item):
    pass

def findPersonByAttributes(item):
    pass

def findPersonById(item):
    _name = item.get("id", None)
    _type = "pmi"

    print('finderPsonByID')
    _response = pmi.pmi_get('2')


    if _name:
        return make_response(
            "{res}".format(res=_response), 200
        )
    else:
        abort(
            406,
            "Item name {name} is null".format(name=_name),
        )
