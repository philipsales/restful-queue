#!/bin/bash

#install couchbase python dependencies 
wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-4-amd64.deb
sudo dpkg -i couchbase-release-1.0-4-amd64.deb
sudo apt-get -y update 
sudo apt-get -y install libcouchbase-dev libcouchbase2-bin build-essential