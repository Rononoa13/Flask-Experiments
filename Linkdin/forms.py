from flask_wtf import Form
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up', validators=[DataRequired()])