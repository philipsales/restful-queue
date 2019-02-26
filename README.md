
## Prerequisites
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| Python       | 3.6.2    |
| Virtualenv   | 15.1.0   |
| Couchbase    | 4.5.1    |
| RabbitMQ     | 3.7.12   |

## Getting started 
1. Create Python virtualenv
    ```bash
    cd producer
    virtualenv --python=<$PATH_TO_PYTHON3.6> resthooks_env/
    ```
1. Activate virtualenv
    ```bash
    source resthooks_env/bin/activate
    ```
1. Install python dependenices 
    ```bash
    pip install requirements.txt
    ```

## Running the Basic 
1. Run resful API 
    ```bash
    cd resthooks_server
    python server.py 
    ```

1. Run receiver/consumper script
    ```bash
    cd resthooks_server/rest_api
    python receiver_logs_topic.py 
    ```

1. Go swagger url
    ```bash
    http://localhost:5000/amqp/ui/
    ```

1. Try out order POST

## Deployment with docker

1. To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t resthooks_server.

# starting up a container
docker run -p 8080:8080 resthooks_server 
```


## Built With
* [Flask-Rest](https://flask-restful.readthedocs.io)

## Contributing
## Versioning 
## Authors
* **Philip Sales** - *adopted work*
## License
This project is licensed under the Creative Commons- see the Types of [Licenses](https://opensource.org/licenses/alphabetical) 
## Acknowledgments
* [Flask-Rest](https://flask-restful.readthedocs.io)

