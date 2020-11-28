import datetime
import os


def clear():
    os.system('export TERM=xterm; clear')  # För att rensa terminalen


def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")  # Tid som t.ex 08:13:45
