from calendar import month_abbr

from file_handling import FileHandling
from helpers import get_weather_file_path


class WeatherFileManager:
    """
    A class for managing weather file operations.
    
    This class provides methods to fetch weather data from CSV files
    for specific months or entire years.
    """
    @classmethod
    def fetch_monthly_weather_file_data(cls, path, month, year):
        month_file_name = get_weather_file_path(path, year, month)
                
        return None if not month_file_name else FileHandling.read_csv_file(month_file_name)

    @classmethod
    def fetch_yearly_weather_files_data(cls, path, year):
        year_data = []
        
        for month in range(1, 13):
            month_weather_data = cls.fetch_monthly_weather_file_data(path, month, year)
            if month_weather_data:
                year_data.append(month_weather_data)

        return year_data
