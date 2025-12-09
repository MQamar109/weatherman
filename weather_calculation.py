from weather_containers import MonthlyAveragesResult, YearlyCalculationResult
from helpers import (find_max_weather_item,
                     find_min_weather_item,
                     find_average_weather_item)

class WeatherCalculation:
    """
    A class for calculating weather statistics and averages.
    
    This class provides methods to calculate average temperature and
    humidity values for a month, as well as the highest and lowest
    temperature and humidity values for an entire year.
    """
    @staticmethod
    def calculate_monthly_temperature_and_humidity_average(monthly_weather_data):
        avg_keys = {
            "avg_max_temp": "max_temperature",
            "avg_min_temp": "min_temperature",
            "avg_mean_humidity": "mean_humidity"
        }

        weather_avg_results = {weather_field: find_average_weather_item(monthly_weather_data, weather_key) for weather_field, weather_key in avg_keys.items()}

        return MonthlyAveragesResult(**weather_avg_results)

    @staticmethod
    def calculate_yearly_temperature_and_humidity_statistics(yearly_weather_data):
        yearly_weather_statistics = {
            "highest_temp": lambda : find_max_weather_item(yearly_weather_data, "max_temperature"),
            "lowest_temp": lambda : find_min_weather_item(yearly_weather_data, "min_temperature"),
            "highest_humidity": lambda : find_max_weather_item(yearly_weather_data, "max_humidity")
        }
    
        calculated_statistics = {
            weather_key : weather_stat_func()
            for weather_key, weather_stat_func in yearly_weather_statistics.items()}

        return YearlyCalculationResult(**calculated_statistics)
