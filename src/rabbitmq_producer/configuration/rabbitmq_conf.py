
#SERVER Configuration
RabbitMQENV = "production"

RabbitMQConfig = {
    'development': {
        'BUCKET': 'awhcurisdb_dev',
        'USERNAME': 'superman',
        'PASSWORD': 'kryptonite',
        'PROTOCOL': 'http',
        'SCHEME': 'RabbitMQ',
        'IP': '172.104.49.91',
        'HOST': 'RabbitMQ://172.104.49.91/',
        'PORT': '8093',
        'TIMEOUT': 72000
    },
    'production': {
        'BUCKET': 'awhdispergodb',
        'USERNAME': 'superman',
        'PASSWORD': 'kryptonite',
        'PROTOCOL': 'http',
        'SCHEME': 'RabbitMQ',
        'IP': '172.104.171.229',
        'HOST': 'RabbitMQ://172.104.171.229/',
        'PORT': '8093',
        'TIMEOUT': 720000
    },
}