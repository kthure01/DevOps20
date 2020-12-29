from tkinter import *

import repo.Utils as Utils
from repo.Weekdays import Weekdays, Months


class CalendarApp:
    def __init__(self, master, month):
        self.root = master
        self.root.geometry('850x540')
        # self.root.resizable(0, 0)
        self.root.title('Månadskalender med namnsdagar')
        self.root.option_add('*font', ('Helvetica', 12))
        self.month = None
        self.root_frm = None
        self.gui_setup(month)

    def gui_setup(self, month):
        self.month = month
        self.frm_setup()
        self.upper_rows_setup()
        self.main_view_setup()

    def frm_setup(self):
        if self.root_frm:
            self.root_frm.destroy()

        self.root_frm = Frame(self.root)
        self.root_frm.pack()

        self.top_frm = Frame(self.root_frm, height=30, relief=GROOVE)
        self.top_frm.pack()

        self.days_frm = Frame(self.root_frm, height=30)
        self.days_frm.pack(fill=BOTH)

        self.left_frm = Frame(self.root_frm, height=400, width=30)
        self.left_frm.pack(side=LEFT, fill=BOTH)

        self.main_frm = Frame(self.root_frm, height=400, width=30)
        self.main_frm.pack(side=LEFT, fill=BOTH, expand=TRUE)

    def upper_rows_setup(self):
        Button(self.top_frm, text='<<', command=self.go_back).grid(row=0, column=0)
        Label(self.top_frm, width=30,
              text=f'{Months(self.month.current_month).name} {self.month.current_year}').grid(row=0, column=1)
        Button(master=self.top_frm, text='>>', command=self.go_forward).grid(row=0, column=2)

        for cnt, day in enumerate(Weekdays._member_names_):
            if 'Dummy' not in day:
                Label(self.days_frm, width=12, text=day, relief=GROOVE).grid(row=0, column=cnt)
            else:
                Label(self.days_frm, width=3).grid(row=0, column=cnt)

    def go_back(self):
        self.gui_setup(self.month.load_previous_month())

    def go_forward(self):
        self.gui_setup(self.month.load_next_month())

    def main_view_setup(self):
        # ('2020-12-01', '49', '2', 'Oskar\nOssian', False, True)
        row = 0
        column = 0
        for _, day in enumerate(self.month.get_day_by_day()):
            if column == 0:
                Label(self.left_frm, width=3, height=4, text=f'v\n{day[1]}', relief=GROOVE) \
                    .grid(row=row, column=column)

            fg = '#0000FF' if day[5] else '#000000'

            column = int(day[2])
            if day[2] == 7 or day[4]:
                Label(self.main_frm, width=12, height=4, text=f'{Utils.get_date_from_string(day[0])}\n{day[3]}',
                      anchor=N, relief=GROOVE, fg=fg, bg='#E61010').grid(row=row, column=column)
            else:
                Label(self.main_frm, width=12, height=4, text=f'{Utils.get_date_from_string(day[0])}\n{day[3]}',
                      anchor=N, relief=GROOVE, fg=fg).grid(row=row, column=column)

            if column == 7:
                row += 1
                column = 0
