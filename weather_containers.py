# Class to store the weather item
class WeatherItem:
    def __init__(self, max_temp, min_temp, max_humidity, mean_humidity, date):
        self.max_temperature = max_temp
        self.min_temperature = min_temp
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.date = date

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f'{self.max_temperature}, {self.mean_humidity}, {self.max_humidity}, {self.min_temperature}'


# Class to store the result of the averages
class MonthlyAveragesResult:
    def __init__(self, avg_max_temp, avg_min_temp, avg_mean_humidity):
        self.average_max_temperature = avg_max_temp
        self.average_min_temperature = avg_min_temp
        self.average_mean_humidity = avg_mean_humidity

    def __str__(self):
        return (f'Highest Average: {self.average_max_temperature}C \n'
                f'Lowest Average: {self.average_min_temperature}C \n'
                f'Average Mean Humidity: {self.average_mean_humidity}%')


# class to store the result of the yearly calculation and date
class YearlyCalculation:
    def __init__(self, highest_temp, highest_temp_date, lowest_temp, lowest_temp_date, highest_humidity,
                 highest_humidity_date):
        self.highest_temp = highest_temp
        self.highest_temp_date = highest_temp_date

        self.lowest_temp = lowest_temp
        self.lowest_temp_date = lowest_temp_date

        self.highest_humidity = highest_humidity
        self.highest_humidity_date = highest_humidity_date

    def __str__(self):
        return (f"Highest: {self.highest_temp}C on "
                f"{self.highest_temp_date['month']} {self.highest_temp_date['day']}\n"
                f"Lowest: {self.lowest_temp}C on "
                f"{self.lowest_temp_date['month']} {self.lowest_temp_date['day']}\n"
                f"Humidity: {self.highest_humidity}% on "
                f"{self.highest_humidity_date['month']} {self.highest_humidity_date['day']}")
