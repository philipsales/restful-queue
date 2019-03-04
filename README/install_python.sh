#!/bin/bash

## Getting started 
# Python       | 3.6.x    |

# install curl 
sudo apt-get update \
  && apt-get install -y software-properties-common curl \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y python3.6 python3.6-venv

#root directory
cd ~/

#create virtual_env folder
mkdir src_venv 

# add permission to virtual_env to current user 
usermod -aG src_venv `id -un`