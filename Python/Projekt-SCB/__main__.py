from tkinter import *

from repo.Helpers import Helpers as hlp
from repo.CalendarGui import CalendarApp as calendar_app
from repo.Month import Month

if __name__ == '__main__':
    root = Tk()
    app = calendar_app(root, Month(hlp.get_current_year(), hlp.get_current_month()))

    root.mainloop()
