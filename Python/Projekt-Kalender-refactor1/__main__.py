from tkinter import *
import repo.CalendarGui as CalendarGui
import repo.Month as Month
import repo.api as api

if __name__ == '__main__':
    root = Tk()
    app = CalendarGui.CalendarApp(root, Month.Month(api.Api()))

    root.mainloop()
