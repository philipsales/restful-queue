
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
    virtualenv --python=<$PATH_TO_PYTHON3.6> src_venv/
    ```

1. Activate virtualenv
    ```bash
    source src_venv/bin/activate
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

# Deployment 
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| Ubuntu       | 16.04LTS |

## Install Docker Repository
1. Installing Repository 
    ```bash
    sudo apt-get update
    ```

1. Installing Packages 
    ```bash
    sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    ```

1. Add Docker’s official GPG key:
    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

1. Verify fingerprints:
    ```bash
    sudo apt-key fingerprint 0EBFCD88
    ```

1. Use the following command to set up the stable repository
    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

## Install Docker-CE 
1. Update apt 
    ```bash
    sudo apt-get update
    ```

1. Install the latest version of Docker CE 
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io 
    ```

## Install Docker 
1. Installing Docker Compose
    1.2. sudo apt-get install docker-compose

## Run using docker

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

