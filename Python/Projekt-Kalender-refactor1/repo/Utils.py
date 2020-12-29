import os
from datetime import datetime


# För att rensa terminalen
def clear():
    os.system('export TERM=xterm; clear')


# Tid som YYYY-MM-DD HH:mm:ss
def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_todays_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def get_current_year() -> int:
    return datetime.now().year


def get_current_month() -> int:
    return datetime.now().month


def get_date_from_string(date) -> int:  # String as YYYY-MM-DD, e.g 2020-12-24
    return datetime.strptime(date, "%Y-%m-%d").day
