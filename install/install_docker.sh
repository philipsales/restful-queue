#!/bin/bash

## Tested on 
# Ubuntu    | 16.04    |
# docker    | 15.1.0   |
# docker-compose    | 1.23.2   |

##INSTALL docker
#Installing Repsoitory 
sudo apt-get update

#Installing Packages 
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

#Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#Verify fingerprints:
sudo apt-key fingerprint 0EBFCD88

#Use the following command to set up the stable repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

#Update apt 
sudo apt-get update

#Install the latest version of Docker CE  = Ubuntu 14.04 LTS
# sudo apt-get install docker-ce docker-ce-cli containerd.io 

#Install the latest version of Docker CE  = Ubuntu 16.04 LTS
sudo apt-get install -y docker-ce

##INSTALL docker-compose
#check latest
sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

#change permission
sudo chmod +x /usr/local/bin/docker-compose