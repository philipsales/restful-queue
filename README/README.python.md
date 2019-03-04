## Prerequisites
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| Python       | 3.6.2    |

## Getting started 
1. update dependencies and packages
    ```bash
    sudo apt-get update \
        && apt-get install -y software-properties-common curl \
        && add-apt-repository ppa:deadsnakes/ppa \
        && apt-get update \
        && apt-get install -y python3.6 python3.6-venv
    ```

1. download specific python version
    ```bash
    wget http://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
    tar xzvf Python-3.6.0.tgz
    cd Python-3.6.0/
    ./configure
    make
    sudo make install
    ```
