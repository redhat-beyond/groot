#!/usr/bin/env bash

apt update

apt install -y python3.7 
apt install -y python3-pip 

pip3 install --upgrade pip
pip3 install Flask 

#go to the directory containing the file we want to run
cd /vagrant/

FLASK_APP=hello.py flask run --host=0.0.0.0
