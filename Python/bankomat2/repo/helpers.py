import datetime
import os


def clear():
    os.system('export TERM=xterm; clear')


def get_timestamp():
    return datetime.datetime.now().strftime("%M:%S")
