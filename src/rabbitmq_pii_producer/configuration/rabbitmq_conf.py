
#SERVER Configuration
RabbitMQENV = "development"

RabbitMQConfig = {
    'development': {
        'EXCHANGE_TYPE': 'topic',
        'USERNAME': 'guest',
        'PASSWORD': 'guest',
        'HOST': 'localhost',
        'TIMEOUT': 15 
    },
    'production': {
        'EXCHANGE_TYPE': 'topic',
        'USERNAME': 'RabbitMQAdmin',
        'PASSWORD': 'RabbitAdm(1)n@AWH',
        'HOST': '172.104.54.251',
        'TIMEOUT': 15 
    },
}