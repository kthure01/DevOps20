from wtforms import Form, validators, StringField


class BankAccountForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=128)])
