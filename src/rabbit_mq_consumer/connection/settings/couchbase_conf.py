
#SERVER Configuration
CouchbaseENV = "production"
#'PORT': '8091' for Web UI  
#'PORT': '8093' for n1ql
#'PORT': '4984' for public sync 
#'PORT': '4985' for admin sync 


CouchbaseConfig = {
    'development': {
        'BUCKET': 'awhcurisdb_dev',
        'USERNAME': 'superman',
        'PASSWORD': 'kryptonite',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '172.104.49.91',
        'HOST': 'couchbase://172.104.49.91/',
        'PORT': '8093',
        'TIMEOUT': 72000
    },
    'production': {
        'BUCKET': 'awhdispergodb',
        'USERNAME': 'superman',
        'PASSWORD': 'kryptonite',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '172.104.171.229',
        'HOST': 'couchbase://172.104.171.229/',
        'PORT': '8093',
        'TIMEOUT': 720000
    },
}