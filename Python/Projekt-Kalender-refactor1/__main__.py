from tkinter import *
from repo.CalendarGui import CalendarApp
from repo.Month import Month
import repo.Utils as Utils

if __name__ == '__main__':
    root = Tk()
    app = CalendarApp(root, Month(Utils.get_current_year(), Utils.get_current_month()))

    root.mainloop()
