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
    def calculate_month_temperature_and_humidity_average(monthly_weather_data):
        avg_keys = {
            "avg_max_temp": "max_temperature",
            "avg_min_temp": "min_temperature",
            "avg_mean_humidity": "mean_humidity"
        }

        results = {field: find_average_weather_item(monthly_weather_data, weather_key) for field, weather_key in avg_keys.items()}


        return MonthlyAveragesResult(**results)

    @staticmethod
    def calculate_yearly_temperature_and_humidity_statistics(yearly_weather_data):
        max_temperature = find_max_weather_item(yearly_weather_data, "max_temperature")
        min_temperature = find_min_weather_item(yearly_weather_data, "min_temperature")
        max_humidity = find_max_weather_item(yearly_weather_data, "max_humidity")

        return YearlyCalculationResult(max_temperature,
                                       min_temperature,
                                       max_humidity)
