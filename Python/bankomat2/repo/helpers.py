import datetime


def clear():
    import os
    os.system('export TERM=xterm; clear')


def is_integer(value):
    return value.isdigit()

def get_timestamp():
    return datetime.datetime.now().strftime("%M:%S")