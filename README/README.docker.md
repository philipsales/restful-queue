
## Prerequisites
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| Ubuntu       | 16.04LTS |
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
