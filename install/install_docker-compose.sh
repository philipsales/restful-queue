#!/bin/bash

## Tested on 
# Ubuntu    | 16.04    |
# docker    | 15.1.0   |
# docker-compose    | 1.23.2   |

#Install the latest version of Docker CE  = Ubuntu 16.04 LTS
sudo apt-get install -y docker-ce

##INSTALL docker-compose
#check latest
sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

#change permission
sudo chmod +x /usr/local/bin/docker-compose