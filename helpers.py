from datetime import datetime
from calendar import month_abbr, month_name
import os

from constants import DATE_FORMAT, BLACK_COLOR, BLUE_COLOR, RED_COLOR


def find_file(path, year, month):
    month_abbreviation = month_abbr[month]
    result = None

    for file_name in os.listdir(path):
        if str(year) in file_name and month_abbreviation in file_name:
            result = os.path.join(path, file_name)
            break

    return result


# Extract month and year
def extract_month_and_year(date_string):
    parts = date_string.split("/")
    year = int(parts[0])
    month = int(parts[1])

    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")

    return month, year


def extract_date_parts(date_str):
    dt = datetime.strptime(date_str, DATE_FORMAT)
    return {
        "day": dt.day,
        "month": dt.month,  # month number (1-12)
        "year": dt.year
    }


# Find Maximum value of any obj value
def find_max_weather_item(weather_items_list, weather_item_key):
    maximum_value = max(weather_items_list, key=lambda weather_item : weather_item[weather_item_key])

    return maximum_value


# Find minimum value of any obj key from a month data
def find_min_weather_item(weather_items_list, weather_item_key):
    minimum_value = min(weather_items_list, key=lambda weather_item : weather_item[weather_item_key])

    return minimum_value


# Find average value
def find_average_weather_item(month_data, obj_key):
    total_value = 0

    for day in month_data:
        if day[obj_key]:
            total_value += day[obj_key]
    count = len(month_data)
    average_value = total_value / count if count > 0 else 0

    return round(average_value)
