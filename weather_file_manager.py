from calendar import month_abbr

from file_handling import FileHandling
from helpers import find_file


class WeatherFileManager:
    @classmethod
    def fetch_file_data(cls, path, month, year):
        file_name = find_file(path, year, month)
                
        return None if not file_name else FileHandling.read_csv_file(file_name)

    @classmethod
    def fetch_year_files_data(cls, path, year):
        year_data = []
        
        for month in range(1, 13):
            month_data = cls.fetch_file_data(path, month, year)
            if month_data:
                year_data.append(month_data)

        return year_data
