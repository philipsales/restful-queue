
#SERVER Configuration
#CouchbaseENV = "development"
CouchbaseENV = "uat"
#'PORT': '8091' for Web UI  
#'PORT': '8093' for n1ql
#'PORT': '4984' for public sync 
#'PORT': '4985' for admin sync 


CouchbaseConfig = {
    'development': {
        'BUCKET': 'awhdispergodb',
        'USERNAME': 'adminadmin',
        'PASSWORD': 'adminadmin',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '127.0.0.1',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '8093',
        'TIMEOUT': 72000
    },
    'uat': {
        'BUCKET': 'awhdispergodb',
        'USERNAME': 'superman',
        'PASSWORD': 'kryptonite',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '139.162.49.49',
        'HOST': 'couchbase://139.162.49.49/',
        'PORT': '8091',
        'TIMEOUT': 720000
    },
}