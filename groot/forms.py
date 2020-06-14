from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from groot.models import User, Policy


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


class UpdateProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[
                             DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[
                            DataRequired(), Length(min=2, max=20)])
    nick_name = StringField('Nickname', validators=[
                            DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Change Photo: ', validators=[
                        FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Save Changes')

    def validate_email(self, email):
        if email.data != current_user.email:
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


class NewPolicyForm(FlaskForm):
    policy_name = StringField('Name', validators=[DataRequired(), Length(
        min=2, max=20)], render_kw={"placeholder": "Policie's name..."})
    plant_type = StringField('Plant Type', validators=[DataRequired(), Length(
        min=2, max=30)], render_kw={"placeholder": "Plant's type..."})
    humidity = FloatField('Humidity', validators=[DataRequired(), NumberRange(0, 100,"Please enter a number between 0 - 100")], render_kw={
                           "placeholder": "Humidity percentage, example value: 15"})
    amount_light = FloatField('Light Amount', validators=[DataRequired(), NumberRange(0, 100,"Please enter a number between 0 - 100")], render_kw={
                               "placeholder": "Light percentage, example value: 15"})
    irregation_frequency = StringField('Irregation Frequency', validators=[
                                       DataRequired()], render_kw={"placeholder": "Times per week"})
    irregation_amount = StringField('Irregation Amount', validators=[
                                    DataRequired()], render_kw={"placeholder": "Litres"})

    submit = SubmitField('Add Policy')

    def validate_policy_name(self, policy_name):
        policy_name = Policy.query.filter_by(
            policy_name=policy_name.data).first()
        if policy_name:
            raise ValidationError(
                'This policy name is taken, please choose a different one.')
