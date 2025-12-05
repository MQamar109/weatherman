from calendar import month_abbr

from file_handling import FileHandling
from helpers import get_file_name


class WeatherFileManager:
    @classmethod
    def fetch_file_data(cls, path, month, year):
        file_name = get_file_name(year, month)
        file_data = FileHandling.read_csv_file(path, file_name)
        return file_data

    @classmethod
    def fetch_year_files_data(cls, path, year):
        year_data = []

        for month in range(1, 13):
            month_data = cls.fetch_file_data(path, month, year)
            if month_data:
                year_data.append(month_data)

        return year_data
