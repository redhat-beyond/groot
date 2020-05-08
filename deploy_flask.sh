#!/usr/bin/env bash

FLASK_PORT=5000

apt update

apt install -y python3.7
apt install -y python3-pip

pip3 install --upgrade pip

pip3 install -r /vagrant/requirements.txt

apt install -y postgresql postgresql-contrib

sudo -u postgres createdb groot

sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'groot';"

export FLASK_APP=/vagrant/run.py
flask run -h 0.0.0.0 -p $FLASK_PORT >> /vagrant/log.txt 2>&1 &
