from datetime import datetime
from calendar import month_abbr, month_name

from constants import DATE_FORMAT, BLACK_COLOR, BLUE_COLOR, RED_COLOR
from file_handling import read_file


# create file ame with year and month
def get_file_name(year, month):
    month_name = month_abbr[month]
    return f'Murree_weather_{year}_{month_name}.txt'


def fetch_file_data(path, year, month):
    file_name = get_file_name(year, month)
    file_data = read_file(path, file_name)
    return file_data


def fetch_year_files_data(path, year):
    year_data = []

    for month in range(1,13):
        month_data = fetch_file_data(path, year, month)
        if month_data:
            year_data.append(month_data)

    return year_data


def fetch_month_file_data(path, date_string):
    month, year = extract_month_and_year(date_string)
    month_data = fetch_file_data(path, year, month)
    return month_data


def print_graph_header(date_string):
    month, year = extract_month_and_year(date_string)
    print(f'{month_name[month]} {year}')


# Extract month and year
def extract_month_and_year(date_string):
    parts = date_string.split('/')
    year = int(parts[0])
    month = int(parts[1])

    if month < 1 or month > 12:
        raise ValueError('Invalid month. Month must be between 1 and 12.')

    return month, year


# Get date format like 24 March 2025
def extract_date_parts(date_str):
    dt = datetime.strptime(date_str, DATE_FORMAT)
    return {'day': dt.day, 'month': dt.strftime('%B'), 'year': dt.year}


# Find Highest value of any obj value
def find_highest_value(month_data, obj_key):
    highest_value = month_data[0][obj_key]
    date = month_data[0]['date']

    for record in month_data:
        if record[obj_key] > highest_value:
            highest_value = record[obj_key]
            date = record['date']

    return {'value': highest_value, **extract_date_parts(date)}


# Find minimum value of any obj key from a month data
def find_lowest_value(month_data, obj_key):
    lowest_value = int(month_data[0][obj_key])
    date = month_data[0]['date']

    for record in month_data:
        if record[obj_key] < lowest_value:
            date = record['date']
            lowest_value = record[obj_key]

    return {'value': lowest_value, **extract_date_parts(date)}

# Find average value
def find_average_value(month_data, obj_key):
    total_value = 0

    for day in month_data:
        if day[obj_key]:
            total_value += day[obj_key]
    count = len(month_data)
    average_value = total_value / count if count > 0 else 0
    return round(average_value)


def draw_separate_bar_graph(month_data):
    for day in month_data:
            date = extract_date_parts(day.date)
            print(date['day'], RED_COLOR, '+' * day.max_temperature + BLACK_COLOR, str(day.max_temperature) + 'C')
            print(date['day'], BLUE_COLOR, '+' * day.min_temperature + BLACK_COLOR, str(day.min_temperature) + 'C')


#Print graph of min and max temp on same line
def draw_combine_bar_graph(month_data):
    for day in month_data:
        date = extract_date_parts(day.date)
        print(date['day'], BLUE_COLOR,
              '+' * day.min_temperature + RED_COLOR + '+' *
              day.min_temperature + BLACK_COLOR,
              str(day.min_temperature) + 'C' + ' - ' +
              str(day.max_temperature) + 'C')