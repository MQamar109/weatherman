import csv
import os

from constants import (
    PKT_DATE,
    PKST_DATE,
    MAX_HUMIDITY,
    MAX_TEMPERATURE,
    MEAN_HUMIDITY,
    MIN_TEMPERATURE,
)
from weather_containers import WeatherItem


def read_file(path, file_name):
    file_path = os.path.join(path, file_name)
    csv_file_data = []

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            data = csv.DictReader(file)
            data.fieldnames = [name.strip() for name in data.fieldnames]
            for row in data:
                weather_item = WeatherItem(date=row.get(PKT_DATE) or row.get(PKST_DATE),
                                           max_temp=int(row[MAX_TEMPERATURE] if row[MAX_TEMPERATURE] else 0),
                                           min_temp=int(row[MIN_TEMPERATURE] if row[MIN_TEMPERATURE] else 0),
                                           mean_humidity=int(row[MEAN_HUMIDITY] if row[MEAN_HUMIDITY] else 0),
                                           max_humidity=int(row[MAX_HUMIDITY] if row[MAX_HUMIDITY] else 0))
                csv_file_data.append(weather_item)

    return csv_file_data
