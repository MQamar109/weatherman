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
    def calculate_month_temperature_and_humidity_average(month_data):
        avg_keys = {
            "avg_max_temp": "max_temperature",
            "avg_min_temp": "min_temperature",
            "avg_mean_humidity": "mean_humidity"
        }

        results = {}
        for field, key in avg_keys.items():
            results[field] = find_average_weather_item(month_data, key)

        return MonthlyAveragesResult(
            avg_max_temp=results["avg_max_temp"],
            avg_min_temp=results["avg_min_temp"],
            avg_mean_humidity=results["avg_mean_humidity"]
        )

    @staticmethod
    def calculate_yearly_temperature_and_humidity_statistics(year_data):
        max_temperature = find_max_weather_item(year_data, "max_temperature")
        min_temperature = find_min_weather_item(year_data, "min_temperature")
        max_humidity = find_max_weather_item(year_data, "max_humidity")

        return YearlyCalculationResult(max_temperature,
                                       min_temperature,
                                       max_humidity)
