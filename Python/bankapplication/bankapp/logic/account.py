from bankapp.models.BankAccount import BankAccount
from bson.objectid import ObjectId


def create_account(name, user):
    account = BankAccount(name=name)
    account.save()

    user.accounts.append(account)
    user.save()

    return account


def get_account(account_id):
    return BankAccount.objects(id=ObjectId(str(account_id))).get()
