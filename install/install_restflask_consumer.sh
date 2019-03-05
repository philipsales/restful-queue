#!/bin/bash

## Tested on 
# Python       | 3.6.2    |
# Virtualenv   | 15.1.0   |

ROOT_SRC="$(pwd)"
SRC_FOLDER="$ROOT_SRC/src"
APP_FOLDER="$SRC_FOLDER/rabbitmq_consumer"

#create root src 
mkdir ~/src

#Create Python virtualenv
cd $ROOT_SRC

virtualenv --python=python3.6 $ROOT_SRC/python_env 

#Activate virtualenv
source $ROOT_SRC/python_env/bin/activate

#Install python dependenices 
pip install -r requirements.txt

## Running the Basic 
cd $APP_FOLDER
python receive_queue.py 
    
#Go swagger url
#http://localhost:5000/basepath/ui/

#TODO: make settings config dynamic


