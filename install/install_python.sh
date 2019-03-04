#!/bin/bash

sudo apt-get -y update 

#install C compiler
sudo apt-get install -y build-essential
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y libssl-dev

wget http://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzvf Python-3.6.2.tgz
cd Python-3.6.2/
./configure
#./configure --enable-optimizations
make
sudo make install

#install python
sudo apt install -y python-pip
sudo pip install virtualenv