
#SERVER Configuration
CouchbaseENV = "local"
#'PORT': '8093' for n1ql
#'PORT': '4984' for public sync 
#'PORT': '4985' for admin sync 


CouchbaseConfig = {
    'local': {
        'BUCKET': 'awhcurisdb_local',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '127.0.0.1',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '8093',
        'TIMEOUT': 72000
    },
    'development': {
        'BUCKET': 'awhcurisdb_dev',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '172.104.49.91',
        'HOST': 'couchbase://172.104.49.91/',
        'PORT': '8093',
        'TIMEOUT': 72000
    },
    'production': {
        'BUCKET': 'awhdispergodb',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '172.104.176.10',
        'HOST': 'couchbase://172.104.176.10/',
        'PORT': '8093',
        'TIMEOUT': 720000
    },
}