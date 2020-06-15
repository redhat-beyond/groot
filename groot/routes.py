import os
import secrets
from PIL import Image
from flask import Flask, Response, render_template, request, redirect, url_for, flash, abort
from run import app, db
from groot.models import *
from groot.forms import RegistrationForm, LoginForm, UpdateProfileForm, NewPolicyForm
from flask_login import login_user, current_user, logout_user, login_required
import hashlib


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
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('index.html', title='Dashboard', image_file=image_file)


@app.route('/policies', methods=['GET', 'POST'])
@login_required
def policies():
    all_policies = Policy.query.all()
    form = NewPolicyForm()
    if form.validate_on_submit():
        newPolicy = Policy(policy_name=form.policy_name.data, plant_type=form.plant_type.data, humidity=form.humidity.data,
                           amount_light=form.amount_light.data, irregation_frequency=form.irregation_frequency.data, irregation_amount=form.irregation_amount.data, writer=current_user.id)
        db.session.add(newPolicy)
        db.session.commit()
        flash("Your policy has been created!", 'success')
        return redirect(url_for('policies'))
    elif request.method == 'POST' and not form.validate_on_submit():
        flash("Wrong policy details, please check in the policy form.", 'danger')
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('policies.html', title='Policies', all_policies=all_policies, form=form, image_file=image_file)


@app.route("/policy/<int:policy_id>/toggle", methods=['POST'])
@login_required
def toggle_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    if policy.writer != current_user.id:
        abort(403)
    policy.is_active = not policy.is_active
    db.session.commit()
    if policy.is_active == True:
        flash('Your Policy has been activated!', 'success')
    else:
        flash('Your Policy has been deactivated!', 'danger')
    return redirect(url_for('policies'))


@app.route("/policy/<int:policy_id>/delete", methods=['POST'])
@login_required
def delete_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    if policy.writer != current_user.id:
        abort(403)
    db.session.delete(policy)
    db.session.commit()
    flash('Your policy has been deleted!', 'success')
    return redirect(url_for('policies'))


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
        flash("Your account has been updated!", 'success')
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
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('sensors.html', title='Sensors', image_file=image_file)


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


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(403)
def not_found(e):
    return render_template("403.html")


@app.errorhandler(500)
def not_found(e):
    return render_template("500.html")
