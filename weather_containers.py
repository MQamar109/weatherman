from calendar import month_abbr

from helpers import extract_date_parts


class WeatherItem:
    """
    A class for representing weather data items.
    
    This class provides methods to store and retrieve weather data
    for a specific day, including maximum temperature, minimum temperature,
    maximum humidity, mean humidity, and date information.
    """
    def __init__(self, max_temp, min_temp, max_humidity, mean_humidity, date):
        self.max_temperature = max_temp
        self.min_temperature = min_temp
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.date = extract_date_parts(date)

    def get_day(self):
        return self.date["day"]

    def get_month(self):
        return self.date["month"]

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __str__(self):
        return (f"{self.max_temperature}, "
                f"{self.mean_humidity}, "
                f"{self.max_humidity}, "
                f"{self.min_temperature}")


class MonthlyAveragesResult:
    """
    A class for storing the result of the monthly averages calculation.
    
    This class provides methods to store and retrieve the result of the monthly averages calculation,
    including the average maximum temperature, average minimum temperature, and average mean humidity.
    """
    def __init__(self, avg_max_temp, avg_min_temp, avg_mean_humidity):
        self.average_max_temperature = avg_max_temp
        self.average_min_temperature = avg_min_temp
        self.average_mean_humidity = avg_mean_humidity

    def __str__(self):
        return (f"Highest Average: {self.average_max_temperature}C \n"
                f"Lowest Average: {self.average_min_temperature}C \n"
                f"Average Mean Humidity: {self.average_mean_humidity}%")


class YearlyCalculationResult:
    """
    A class for storing the result of the yearly calculation.
    
    This class provides methods to store and retrieve the result of the yearly calculation,
    including the highest temperature, lowest temperature, and highest humidity.
    """
    def __init__(self, highest_temp, lowest_temp, highest_humidity):
        self.highest_temp = highest_temp
        self.lowest_temp = lowest_temp
        self.highest_humidity = highest_humidity

    def __str__(self):
        return (f"Highest: {self.highest_temp.max_temperature}C on "
                f"{month_abbr[self.highest_temp.get_month()]} "
                f"{self.highest_temp.get_day()} \n"                
                f"Lowest: {self.lowest_temp.min_temperature}C on "
                f"{month_abbr[self.lowest_temp.get_month()]} "
                f"{self.lowest_temp.get_day()} \n"
                f"Humidity: {self.highest_humidity.max_humidity}% on "
                f"{month_abbr[self.highest_humidity.get_month()]} "
                f"{self.highest_humidity.get_day()}")
