from flask import Flask, Response, render_template, request, redirect, url_for, flash
import groot
from groot.models import User


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
            password = request.form.get('password')
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
            email = request.form.get('email')
            password = request.form.get('password')
            password_repeat = request.form.get('password_repeat')
            user = User(username=first_name)
            db.session.add(user)
            db.session.commit()
            return render_template('login.html')
        except:
            return '<Error: groot_register[POST]>'
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
