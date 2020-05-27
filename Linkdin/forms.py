from flask_wtf import Form
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    firstname = StringField('First Name', validators=[DataRequired("Please Enter your first name.")])
    lastname = StringField('Last Name', validators=[DataRequired("Please Enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please Enter your email address."), Email("Please enter your correct email")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter your correct password."), Length(min=8, message="Password must be 8 character or more.")])
    submit = SubmitField('Sign Up', validators=[DataRequired()])