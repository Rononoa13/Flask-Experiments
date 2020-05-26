from flask_wtf import Form
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
    firstname = StringField('First Name', validators=[DataRequired("Please Enter your first name.")])
    lastname = StringField('Last Name', validators=[DataRequired("Please Enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please Enter your correct email.")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter your correct password.")])
    submit = SubmitField('Sign Up', validators=[DataRequired()])