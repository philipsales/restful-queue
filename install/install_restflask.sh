#!/bin/bash

ROOT_SRC="$(pwd)"
SRC_FOLDER="$ROOT_SRC/src"
APP_FOLDER="$SRC_FOLDER/rabbit_mq_api"

## Getting started 
# Python       | 3.6.2    |
# Virtualenv   | 15.1.0   |

#create root src 
mkdir ~/src

#Create Python virtualenv
cd $ROOT_SRC
virtualenv --python=python3.6 $ROOT_SRC/python_env 

#Activate virtualenv
source $ROOT_SRC/python_env/bin/activate

#Install python dependenices 
pip install requirements.txt

## Running the Basic 
#Run resful API 
cd $ROOT_SRC/$APP_FOLDER
python app.py 
    
#Go swagger url
#http://localhost:5000/basepath/ui/


#TODO
#GIT CLONE FROM SOURCE
