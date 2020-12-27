import requests


class Month():

    def __init__(self, year, month):
        self.uri = 'https://sholiday.faboul.se/dagar/v2.1'
        self.uri_data = None
        self.iter_cnt = 0
        self.current_year = 0
        self.current_month = 0
        self.load_month_data(year, month)

    def load_month_data(self, year, month):
        self.iter_cnt = 0
        self.get_month_data(self.uri, year, month)

    def get_month_data(self, uri, year, month):
        try:
            data = requests.get(f'{uri}/{year}/{month}')
            if data.status_code == 200:
                self.uri_data = data.json()
                self.current_year = year
                self.current_month = month

        except:
            pass

    def load_previous_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1

        self.load_month_data(self.current_year, self.current_month)
        return self

    def load_next_month(self):
        if self.current_month == 12:
            self.current_year += 1
            self.current_month = 1
        else:
            self.current_month += 1

        self.load_month_data(self.current_year, self.current_month)
        return self

    def get_all_days_in_month(self):
        return self.uri_data['dagar']

    def get_start_day_in_week(self):
        all_days = self.get_all_days_in_month()
        return int(all_days[0]['dag i vecka'])

    def get_start_week(self):
        all_days = self.get_all_days_in_month()
        return int(all_days[0]['vecka'])

    def get_number_of_days_in_month(self):
        return len(self.get_all_days_in_month())

    def get_day_by_day(self):
        while self.iter_cnt < self.get_number_of_days_in_month():
            cur, self.iter_cnt = self.iter_cnt, self.iter_cnt + 1

            cur_day = self.uri_data['dagar'][cur]
            date = cur_day['datum']
            week = cur_day['vecka']
            day_in_week = cur_day['dag i vecka']
            names = '\n'.join(cur_day['namnsdag'])
            red_day = 'Ja' in cur_day['röd dag']

            yield (date, week, day_in_week, names, red_day)
