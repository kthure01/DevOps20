from wtforms import Form, StringField, validators, PasswordField


class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=128)])
    password = PasswordField('Password', [validators.Length(min=3)])
