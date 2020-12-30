import json
import requests
import repo.Utils as Utils


class Api:
    # {0} is year and {1} is month
    uri = 'https://sholiday.faboul.se/dagar/v2.1/{0}/{1}'

    def __init__(self, year=Utils.get_current_year(), month=Utils.get_current_month()):
        self.year = year
        self.month = month
        self.data = self.get_month_data()

    def reload(self, year, month):
        self.__init__(year, month)

        return self

    def get_month_data(self) -> str:
        try:
            data = requests.get(self.uri.format(self.year, self.month))
            if data.status_code == 200:
                return data.json()
            else:
                raise ValueError(data.text)

        except ValueError as ve:
            print(f'ERROR: {ve}')

        except IndexError as ie:
            print(f'ERROR: {ie}')

        return ''

    def get_data(self) -> str:
        return self.data

    def print_formatted_data(self):
        print(json.dumps(self.data, indent=3, ensure_ascii=False))
