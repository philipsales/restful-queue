#!/bin/bash

USERNAME='RabbitMQAdmin'
PASSWORD='RabbitAdm(1)n@AWH'

sudo apt-get update

#Sign Key
sudo apt-key adv --keyserver "hkps.pool.sks-keyservers.net" --recv-keys "0x6B73A36E6026DFCA"

#download key
wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | sudo apt-key add -

#enable https transport
sudo apt-get install apt-transport-https

#add apt list
sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list <<EOF
deb https://dl.bintray.com/rabbitmq-erlang/debian xenial erlang
deb https://dl.bintray.com/rabbitmq/debian xenial main
EOF

#install by update
sudo apt-get -y update

#install rabbitmq
sudo apt-get install -y rabbitmq-server

#start
sudo service rabbitmq-server start

#enable managment UI plugin
rabbitmq-plugins enable rabbitmq_management

#change ownership 
sudo chown -R rabbitmq:rabbitmq /var/lib/rabbitmq/

#create managment UI admin user 
sudo rabbitmqctl add_user $USERNAME $PASSWORD
sudo rabbitmqctl set_user_tags $USERNAME administrator
sudo rabbitmqctl set_permissions -p / $USERNAME ".*" ".*" ".*"


#TODO
#Start rabbitmq systemcd
#monitoring and logging for rabbitmq