
#SERVER Configuration
ApiENV = "development"

ApiConfig = {
    'development': {
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'HOST': 'localhost',
        'PORT': '5000',
        'DEBUG': True,
        'TIMEOUT': 7200
    },
    'production': {
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'HOST': '',
        'PORT': '5000',
        'DEBUG': False,
        'TIMEOUT': 7200
    },
}