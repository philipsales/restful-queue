import json
import os 
import sys
import requests
import pprint
from xml.etree import ElementTree
import xmltodict

from requests.exceptions import ConnectionError, RequestException 

from connections.settings.base_conf import pmi_config 

import logging
logger = logging.getLogger("openEmpi")

conn = pmi_config.PatientMasterIndexConfig[pmi_config.PmiENV]

URL = conn['HOST']  
IP_ADDRESS = conn['IP'] 
TIMEOUTE = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']

def pmi_gets(data):
    print(data)

def pmi_get(data):
    headers = _conn_headers()
    url = _conn_url()

    try:
        print(url)
        r = requests.get(url, headers = headers)
        print('===RAW===')
        print(r.status_code)
        print(type(r))

        print('===ELEMTREE===')
        _xml_elem = (ElementTree.fromstring(r.content))
        print(type(_xml_elem))
        print(_xml_elem[0])
        print(json.dumps(xmltodict.parse(r.content)))
        json_response = json.dumps(xmltodict.parse(r.content))

        print('===xmltoDcit===')
        pp = pprint.PrettyPrinter(indent=4)
        my_xml = """
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <audience>
            <name>Philip</name>
        </audience>
        """
        print(type(my_xml))

        #pp.pprint(json.dumps(xmltodict.parse(my_xml)))


        logger.info(r.status_code)
        logger.info(r.elapsed.total_seconds())

    except (ConnectionError, RequestException) as err: 
        logger.error(err) 
        sys.exit(1)

    return json_response 

def push_couchbase(data):
    url_bulk_docs = _conn_url(api_endpoint="_bulk_docs")

    _bulk_push_to_couchbase(conn, url_bulk_docs, data['new_data'])



def _bulk_push_to_couchbase(conn, url, data):
    try:

        couchbase_json = {
            "docs": data,
            "new_edits": True
        }
        
        couchbase_json = json.dumps(couchbase_json)

        r = requests.post(url, 
            data=couchbase_json, 
            headers={"Accept":"application/json",
                "Content-type":"application/json"})
                
        logger.info(r.status_code)
        logger.info(r.elapsed.total_seconds())
        logger.info(r.text)


        return r

    except (ConnectionError, RequestException) as err: 
        logger.error(err) 
        sys.exit(1) 


def _conn_headers():
    #TODO make dynamic pass kwargs
    return {
        "OPENEMPI_SESSION_KEY": "06BA98652F157D407E4FB97E9ADAFB95",
        "Content-Type": "application/xml"
    }

def _conn_filters(**kwargs):
    #TODO make dynamic pass kwargs
    return  {
        "access" : "false",
        "channels": "false",
        "include_docs": "true",
        "revs": "false",
        "update_seq": "false",
        "limit":"5",
        "since":"200"
    }

def _conn_url(**kwargs):
    protocol = PROTOCOL
    ip_address = IP_ADDRESS
    port = PORT 
    urls = "http://localhost:8080/openempi-admin/openempi-ws-rest/person-query-resource/loadPerson?personId=1"

    return urls

if __name__ == "__main__":
    init_couchbase()

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        doc = row["doc"]
        doc["cb_id"] = doc.pop('_id')
        data.append(json.dumps(doc))
        counter += 1
        logger.info(counter)

    return data