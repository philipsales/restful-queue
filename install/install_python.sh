#!/bin/bash

sudo apt-get -y update 

#install C compiler
sudo apt-get install -y build-essential
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y python3-dev


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


#install couchbase python dependencies 
wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-4-amd64.deb
sudo dpkg -i couchbase-release-1.0-4-amd64.deb
sudo apt-get update
sudo apt-get install libcouchbase-dev libcouchbase2-bin 
sudo apt-get install libcouchbase-dev libcouchbase2-bin build-essential