#!/bin/bash

## Getting started 
# Python       | 3.6.x    |

# install curl , python, python-virtualenv
sudo apt-get -y update 
sudo apt-get install -y software-properties-common curl 
#sudo add-apt-repository ppa:deadsnakes/ppa 
sudo add-apt-repository -y ppa:jonathonf/python-3.6
sudo apt-get -y update 
sudo apt-get install -y python3.6 
sudo apt-get install -y python3.6-venv


#install python venv
sudo apt-get install -y python-virtualenv

#root directory
#cd ~/

# add permission to virtual_env to current user 
#usermod -aG `id -un` python_venv


