import csv
import os
from weather_containers import WeatherItem
from constants import MAX_TEMPERATURE, MIN_TEMPERATURE, MEAN_HUMIDITY, MAX_HUMIDITY, DATE


def read_file(path, file_name):
    file_path = os.path.join(path, file_name)
    csv_file_data = []

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            data = csv.DictReader(file)
            data.fieldnames = [name.strip() for name in data.fieldnames]

            for row in data:
                weather_item = WeatherItem(date=row[DATE],
                                           max_temp=int(row[MAX_TEMPERATURE] if row[MAX_TEMPERATURE] else 0),
                                           min_temp=int(row[MIN_TEMPERATURE] if row[MIN_TEMPERATURE] else 0),
                                           mean_humidity=int(row[MEAN_HUMIDITY] if row[MEAN_HUMIDITY] else 0),
                                           max_humidity=int(row[MAX_HUMIDITY] if row[MAX_HUMIDITY] else 0))
                csv_file_data.append(weather_item)
    else:
        print(f'File does not exist {file_path}')

    return csv_file_data
