import datetime
import os


class Helpers:
    # För att rensa terminalen
    @staticmethod
    def clear():
        os.system('export TERM=xterm; clear')

    # Tid som YYYY-MM-DD HH:mm:ss
    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
