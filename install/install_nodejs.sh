#!/bin/bash

## Tested on 
# Ubuntu    | 16.04    |
# node  | v6.16.0    |
# pm2   | 3.3.1  |

#install the NodeSource PPA
cd ~
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh

#PPA will be added to your configuration and your local package cache will be updated automatically. 
sudo bash nodesource_setup.sh


sudo apt-get install -y nodejs

#install compiling code 
sudo apt-get install -y build-essential


#install pm2
npm install -g pm2

#start app.py using pm2 
#pm2 start app.py --interpreter=/root/restful-queue/python_env/bin/python