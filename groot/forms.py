from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Last Name"})
    nickname = StringField('Nickname', validators=[
                           DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Nickname"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email Address"})
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=2, max=50)])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')
