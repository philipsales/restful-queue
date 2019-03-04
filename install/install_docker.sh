#!/bin/bash

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

#Install the latest version of Docker CE 
sudo apt-get install docker-ce docker-ce-cli containerd.io 