import os
from datetime import datetime


class Helpers:
    # För att rensa terminalen
    @staticmethod
    def clear():
        os.system('export TERM=xterm; clear')

    # Tid som YYYY-MM-DD HH:mm:ss
    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_current_year():
        return datetime.now().year

    @staticmethod
    def get_current_month():
        return datetime.now().month

    @staticmethod
    def get_date_from_string(date):  # String as YYYY-MM-DD, e.g 2020-12-24
        return datetime.strptime(date, "%Y-%m-%d").day

# current date and time
# print(datetime.now())
# print(datetime.now().strftime("%H:%M:%S"))
# print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

# print(Helpers.get_date_from_string('2020-12-24'))