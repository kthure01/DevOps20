import json
import repo.Utils as Utils


class Month:

    def __init__(self, api):
        self.api = api
        self.iter_cnt = 0
        self.today = Utils.get_todays_date()


    def load_previous_month(self):

        if self.api.month == 1:
            new_month = 12
            new_year = self.api.year - 1
        else:
            new_month = self.api.month - 1
            new_year = self.api.year

        self.__init__(self.api.reload(new_year, new_month))

        return self

    def load_next_month(self):
        if self.api.month == 12:
            new_year = self.api.year + 1
            new_month = 1
        else:
            new_month = self.api.month + 1
            new_year = self.api.year

        self.__init__(self.api.reload(new_year, new_month))

        return self

    def get_all_days_in_month(self) -> list:
        return self.api.get_data()['dagar']

    def get_start_day_in_week(self) -> int:
        all_days = self.get_all_days_in_month()
        return int(all_days[0]['dag i vecka'])

    def get_start_week(self) -> int:
        all_days = self.get_all_days_in_month()
        return int(all_days[0]['vecka'])

    def get_number_of_days_in_month(self) -> int:
        return len(self.get_all_days_in_month())

    def get_day_by_day(self):
        while self.iter_cnt < self.get_number_of_days_in_month():
            cur, self.iter_cnt = self.iter_cnt, self.iter_cnt + 1

            cur_day = self.api.get_data()['dagar'][cur]
            date = cur_day['datum']
            week = cur_day['vecka']
            day_in_week = cur_day['dag i vecka']
            names = '\n'.join(cur_day['namnsdag'])
            red_day = 'Ja' in cur_day['röd dag']
            today = self.today == date

            yield (date, week, day_in_week, names, red_day, today)



# k = Month(2020, 12)
# print(k.formatted_print())