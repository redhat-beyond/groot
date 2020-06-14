import os
import secrets
from PIL import Image
from flask import Flask, Response, render_template, request, redirect, url_for, flash, abort
from run import app, db
from groot.models import *
from groot.forms import RegistrationForm, LoginForm, UpdateProfileForm
from flask_login import login_user, current_user, logout_user, login_required
import hashlib

user_policies = [
    {
        'name': 'Policy 1',
        'plant_type': 'Mushrooms',
        'humidity': '0.15',
        'light': '0.73',
        'irregation_frequency': '4',
        'irregation_amount': '0.4',
        'sensors': '3',
        'date_created': '03.05.2020',
        'id': '134623415',
        'status': 'True'
    },
    {
        'name': 'Policy 1',
        'plant_type': 'Mushrooms',
        'humidity': '0.15',
        'light': '0.73',
        'irregation_frequency': '4',
        'irregation_amount': '0.4',
        'sensors': '3',
        'date_created': '03.05.2020',
        'id': '134623415',
        'status': 'True'
    },
    {
        'name': 'Policy 2',
        'plant_type': 'Apple Tree',
        'humidity': '0.24',
        'light': '0.68',
        'irregation_frequency': '3',
        'irregation_amount': '0.5',
        'sensors': '2',
        'date_created': '06.07.2020',
        'id': '123423516',
        'status': 'False'
    },
    {
        'name': 'Policy 1',
        'plant_type': 'Mushrooms',
        'humidity': '0.15',
        'light': '0.73',
        'irregation_frequency': '4',
        'irregation_amount': '0.4',
        'sensors': '3',
        'date_created': '03.05.2020',
        'id': '134623415',
        'status': 'True'
    },
    {
        'name': 'Policy 2',
        'plant_type': 'Apple Tree',
        'humidity': '0.24',
        'light': '0.68',
        'irregation_frequency': '3',
        'irregation_amount': '0.5',
        'sensors': '2',
        'date_created': '06.07.2020',
        'id': '123423516',
        'status': 'False'
    }
]


@app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == create_encrypted_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = create_encrypted_password(form.password.data)
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    nick_name=form.nick_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('index.html', title='Dashboard')


@app.route('/policies', methods=['GET', 'POST'])
@login_required
def policies():
    return render_template('policies.html', title='Policies', user_policies=user_policies)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        current_user.nick_name = form.nick_name.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash("Yout account has been updated!", 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.nick_name.data = current_user.nick_name
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)


@app.route('/sensors', methods=['GET', 'POST'])
@login_required
def sensors():
    return render_template('sensors.html', title='Sensors')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


def create_encrypted_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)
    output_size = (180, 180)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    i.save(picture_path)
    return picture_fn
