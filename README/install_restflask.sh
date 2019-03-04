#!/bin/bash

## Getting started 
# Python       | 3.6.2    |
# Virtualenv   | 15.1.0   |

#Create Python virtualenv
cd src 
virtualenv --python=<$PATH_TO_PYTHON3.6> src_venv/

#Activate virtualenv
source src_venv/bin/activate

#Install python dependenices 
pip install requirements.txt

## Running the Basic 
#Run resful API 
cd src 
python app.py 
    
#Go swagger url
#http://localhost:5000/basepath/ui/
