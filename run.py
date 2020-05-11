from flask import Flask, Response, render_template, request, redirect, url_for, flash
import groot
from groot.models import *


app = groot.app
db = groot.db
db.create_all()
db.session.commit()


@app.route("/")
@app.route("/home")
def home():
    return 'Groot Landing Page'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            hash_pw = request.form.get('password')
            #hash check
            
            emailCounter = User.query.filter_by(email = email).count()

            if emailCounter < 1:
                return render_template('error.html',message = 'User not exist')
            else:
                #check_password_hash(pwhash,password)
                count = User.query.filter_by(email=email,hash_pw=hash_pw).count()
                if count > 0:
                    return render_template('error.html',message = 'Welcome user')
                else:
                    return render_template('error.html',message = 'Incorrect password')

            return render_template('register.html')  
        except:
            return '<Error: groot_login[POST]>'
    else:
        return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            nick_name = request.form.get('nickname')
            email = request.form.get('email')
            password = request.form.get('password')
            password_repeat = request.form.get('password_repeat')
            hash_pw = request.form.get('password')

            #is string empty validation
            if not first_name:
              return render_template('error.html',message = 'must provide first_name') 
            elif not last_name:
              return render_template('error.html',message = 'must provide last_name')
            elif not nick_name:
                return render_template('error.html',message = 'must provide nick name')
            elif not email:
                return render_template('error.html',message = 'must provide email')
            elif not password:
               return render_template('error.html',message ="must provide password")
            elif not password_repeat:
                return render_template('error.html',message ="must confirm password")
            #compare password to confirmation password
            elif password_repeat != password:
                return render_template('error.html',message ="passwords don't match")

            emailCounter = User.query.filter_by(email = email).count()
            if emailCounter > 0:
                return render_template('error.html',message = "Email already exist -please use another one")
                
            #hash function hashed_password = generate_password_hash(password)
            user = User(email=email,first_name=first_name,last_name=last_name,nick_name=nick_name,hash_pw=hash_pw)
            db.session.add(user)
            db.session.commit()
            return render_template('login.html')
        except:
            return '<Error: groot_register[POST]>'
    else:
        return render_template('register.html')

@app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('error.html',message = 'from rout')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
