
echo "**** installing updates... ****"
sudo apt update
sudo apt install software-properties-common

echo "**** installing python 3.7... ****"
echo -ne '\n' | sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.7 
sudo apt-get install -y python-pip 
sudo pip install --upgrade pip 

echo "**** installing flask framework... ****"
sudo pip install Flask 
sudo mkdir flask-server && cd flask server
sudo touch hello.py

sudo cat > hello.py <<EOL
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return Response("Hello World!"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
EOL

echo "**** initializing flask-server... ****"
FLASK_APP=hello.py flask run --host=0.0.0.0
