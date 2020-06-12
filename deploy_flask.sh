#!/usr/bin/env bash
FLASK_PORT=5000

# Installing packages
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib
 
pip3 install --upgrade pip
pip3 install -r /vagrant/requirements.txt

# DB creation
sudo -u postgres createdb groot
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'groot';"

export FLASK_APP=/vagrant/run.py
export FLASK_ENV=development
flask run -h 0.0.0.0 -p $FLASK_PORT >> /vagrant/log.txt 2>&1 &
