#!/usr/bin/env bash

TARGET="hello.py"

apt update

apt install -y python3.7 
apt-get install -y python-pip 

pip install --upgrade pip 
pip install Flask 

#go to the directory containing the file we want to run
cd ..; cd ..; cd vagrant

FLASK_APP=$TARGET flask run --host=0.0.0.0
