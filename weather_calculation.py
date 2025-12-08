from weather_containers import MonthlyAveragesResult, YearlyCalculationResult
from helpers import (find_max_weather_item,
                     find_min_weather_item,
                     find_average_weather_item)

class WeatherCalculation:
    @staticmethod
    def calculate_month_temperature_and_humidity_average(month_data):
        avg_highest_temperature = find_average_weather_item(month_data,
                                                     "max_temperature")
        avg_lowest_temperature = find_average_weather_item(month_data,
                                                    "min_temperature")
        avg_mean_humidity = find_average_weather_item(month_data,
                                                      "mean_humidity")

        return MonthlyAveragesResult(avg_max_temp=avg_highest_temperature,
                                         avg_min_temp=avg_lowest_temperature,
                                         avg_mean_humidity=avg_mean_humidity)

    @staticmethod
    def calculate_yearly_temperature_and_humidity_statistics(year_data):
        max_temperature = find_max_weather_item(year_data, "max_temperature")
        min_temperature = find_min_weather_item(year_data, "min_temperature")
        max_humidity = find_max_weather_item(year_data, "max_humidity")

        return YearlyCalculationResult(max_temperature,
                                       min_temperature,
                                       max_humidity)
