#!/usr/bin/env bash

apt update

apt install -y python3.7 
apt install -y python3-pip 

pip3 install --upgrade pip
pip3 install Flask 

apt install -y postgresql postgresql-contrib

cd /vagrant/

FLASK_APP=hello.py
sudo python3 hello.py >> log.txt 2>&1 &

exit 0