import datetime
import os


# För att rensa terminalen
def clear():
    os.system('export TERM=xterm; clear')


# Tid som YYYY-MM-DD HH:mm:ss
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
