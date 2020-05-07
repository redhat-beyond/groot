#!/usr/bin/env bash
FLASK_PORT=5000

# Installing packages
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib
 
pip3 install --upgrade pip
pip3 install -r /vagrant/requirements.txt

export FLASK_APP=/vagrant/hello.py
flask run -h 0.0.0.0 -p $FLASK_PORT >> /vagrant/log.txt 2>&1 &
