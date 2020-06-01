from flask import Flask, Response, render_template, request, redirect, url_for, flash
from run import app, db
from groot.models import *
import hashlib


@app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')    
            user = User.query.filter_by(email=email).first()
            if user:
                hash_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
                if user.password == hash_pw:
                    return redirect(url_for('dashboard'))  
                else:
                    flash('Inccorect password! Please try again.', 'danger')
            else:      
                flash('Inccorect email! Please try again.', 'danger')    
            return redirect(url_for('login'))  
        except:
            return 'Should return 404 error page'
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

            hash_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            user = User(email=email,first_name=first_name,last_name=last_name,nick_name=nick_name,password=hash_pw)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        except:
            return 'Should return 404 error page'
    else:
        return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('index.html', title='Dashboard')


@app.route('/policies', methods=['GET', 'POST'])
def policies():
    return render_template('policies.html', title='Policies')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/sensors', methods=['GET', 'POST'])
def sensors():
    return render_template('sensors.html', title='Sensors')

	