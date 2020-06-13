from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from groot.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Last Name"})
    nick_name = StringField('Nickname', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Nickname"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email Address"})
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError(
                'That email is taken, please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email Address"})
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')
