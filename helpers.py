from datetime import datetime
from constants import MONTH_NUMBER, DATE_FORMAT


# create file ame with year and month
def get_file_name(year, month):
    return f"Murree_weather_{year}_{MONTH_NUMBER[month]}.txt"


# Extract month and year
def extract_year_month(date_string):
    parts = date_string.split('/')
    year = int(parts[0])
    month = int(parts[1])

    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")

    return month, year


# Get date format like 24 March 2025
def extract_date_parts(date_str):
    dt = datetime.strptime(date_str, DATE_FORMAT)
    return {'day': dt.day, 'month': dt.strftime('%B'), 'year': dt.year}


# Find Highest value of any entity
def find_entity_highest_value(month_data, entity):
    if not month_data:
        return "Month data is empty"

    highest_value = month_data[0][entity]
    date = month_data[0]['date']

    for record in month_data:
        if record[entity] > highest_value:
            highest_value = record[entity]
            date = record['date']

    return {'value': highest_value, **extract_date_parts(date)}


# Find minimum value of any entity
def find_entity_lowest_value(month_data, entity):
    if not month_data:
        return "Month data is empty"

    lowest_value = int(month_data[0][entity])
    date = month_data[0]['date']

    for record in month_data:
        if record[entity] < lowest_value:
            date = record['date']
            lowest_value = record[entity]

    return {'value': lowest_value, **extract_date_parts(date)}


# Find average value of any entity
def find_average_entity_value(month_data, entity):
    if not month_data:
        return 0
    total_value = 0

    for day in month_data:
        if day[entity]:
            total_value += day[entity]

    average_value = total_value / len(month_data) if len(month_data) > 0 else 0
    return round(average_value)
