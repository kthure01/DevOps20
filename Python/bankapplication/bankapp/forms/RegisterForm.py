from wtforms import Form, StringField, validators, PasswordField


class RegisterForm(Form):
    firstname = StringField('Firstname', [validators.Length(min=3, max=100)])
    lastname = StringField('Lastname', [validators.Length(min=3, max=100)])
    email = StringField('Email', [validators.Length(min=6, max=128)])
    password = PasswordField('Password', [validators.Length(min=3)])
