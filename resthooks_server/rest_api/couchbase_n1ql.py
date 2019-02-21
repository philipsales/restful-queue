import json
import os 
import sys
import datetime as dt
import uuid

from couchbase.cluster import Cluster, PasswordAuthenticator
from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError, CouchbaseError, CouchbaseNetworkError, NotFoundError

from settings.base_conf import couchbase_config

import logging
logger = logging.getLogger("couchbase.n1q1")

conn = couchbase_config.CouchbaseConfig[couchbase_config.CouchbaseENV]

USERNAME = conn['USERNAME'] 
PASSWORD = conn['PASSWORD'] 
BUCKET = conn['BUCKET'] 
HOST = conn['HOST'] 
URL = HOST + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']


def couchbase_get():
    try:
        statement = _set_statement()
        logger.info(statement)
        
    except FileNotFoundError:
        logger.info(statement)

    res = _get_all(statement)
    #return _dict2json(res, True)
    return res
    #res = _insert_document(statement)
    #return res

def _set_statement(**kwargs):
    statement = ("INSERT INTO " + BUCKET + " (KEY, VALUE) "
                 + "VALUES ( '_opencart:order:" + str(uuid.uuid4()) + "',"
                 + " { 'id' : '01' }) RETURNING *;")

    #statement = ("SELECT * from `awhcurisdb_local` awh") 
    return statement 

def _authenticate():
    cluster = Cluster(HOST)
    authenticator = PasswordAuthenticator(USERNAME, PASSWORD)
    cluster.authenticate(authenticator)
    bucket = cluster.open_bucket(BUCKET)
    return bucket

def _get_all(statement): 
    print(statement)
    try:
        #bucket = _authenticate()
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT
        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 
        results = bucket.n1ql_query(query)

        results = []
        for row in bucket.n1ql_query(query):
            results.append(row)
        print(results)

    except (CouchbaseError, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.info(err)
        sys.exit(1)

    return results

def _insert_document(statement): 
    print('insert')
    try:
        #bucket = _authenticate()
        bucket = Bucket(URL)
        result = bucket.insert('document_name', {'some': 'value'})
        print(result)

    except (CouchbaseError, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.info(err)
        sys.exit(1)

    return result

def _dict2json(results, is_etl):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    return data
#run as standalone module
if __name__ == "__main__":
    couchbase_get()