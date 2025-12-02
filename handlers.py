from file_handling import read_file
from constants import RED_COLOR, BLUE_COLOR, BLACK_COLOR
from helpers import find_entity_lowest_value, find_entity_highest_value, get_file_name, find_average_entity_value, \
    extract_year_month, extract_date_parts
from weather_containers import MonthlyAveragesResult, YearlyCalculation


# Find the highest and lowest temperature and most humidity
def find_year_highest_temp_humidity_and_lowest_temp(year_data):
    first_month = year_data[0]
    highest_temp = find_entity_highest_value(first_month, 'max_temperature')
    lowest_temp = find_entity_lowest_value(first_month, 'min_temperature')
    highest_humidity = find_entity_highest_value(first_month, 'max_humidity')

    for month in year_data[1:]:
        high_temperature = find_entity_highest_value(month, 'max_temperature')
        if high_temperature['value'] > highest_temp['value']:
            highest_temp = high_temperature

        low_temperature = find_entity_lowest_value(month, 'min_temperature')
        if low_temperature['value'] < lowest_temp['value']:
            lowest_temp = low_temperature

        high_humidity = find_entity_highest_value(month, 'max_humidity')
        if high_humidity['value'] > highest_humidity['value']:
            highest_humidity = high_humidity

    return {'highest_temp': highest_temp, 'lowest_temp': lowest_temp, 'highest_humidity': highest_humidity}


def calculate_month_averages(path, date_string):
    month, year = extract_year_month(date_string)
    file_name = get_file_name(year, month)
    file_data = read_file(path, file_name)

    if file_data:
        avg_highest_temperature = find_average_entity_value(file_data, 'max_temperature')
        avg_lowest_temperature = find_average_entity_value(file_data, 'min_temperature')
        avg_mean_humidity = find_average_entity_value(file_data, 'mean_humidity')
        averages = MonthlyAveragesResult(avg_max_temp=avg_highest_temperature, avg_min_temp=avg_lowest_temperature,
                                         avg_mean_humidity=avg_mean_humidity)
        print(averages)


def get_year_calculations_and_date(path, year):
    year_data = []

    for month in range(12):
        file_name = get_file_name(year, month + 1)
        file_data = read_file(path, file_name)
        if file_data:
            year_data.append(file_data)

    if year_data:
        data = find_year_highest_temp_humidity_and_lowest_temp(year_data)
        max_temp, min_temp, max_humidity = data['highest_temp'], data['lowest_temp'], data['highest_humidity']
        calculated_avg = YearlyCalculation(highest_temp=max_temp['value'],
                                           highest_temp_date={'day': max_temp['day'], 'month': max_temp['month']},

                                           lowest_temp=min_temp['value'],
                                           lowest_temp_date={'day': min_temp['day'], 'month': min_temp['month']},

                                           highest_humidity=max_humidity['value'],
                                           highest_humidity_date={'day': max_humidity['day'],'month': max_humidity['month']})
        print(calculated_avg)
    else:
        print('Not any File of this year found!')


# Draw horizontal bar graph on separate lines
def draw_horizontal_bar_graph(path, date_string):
    month, year = extract_year_month(date_string)
    file_name = get_file_name(year, month)
    file_data = read_file(path, file_name)

    if file_data:
        date = extract_date_parts(file_data[0].date)
        print(date['month'], date['year'])

        for day in file_data:
            date = extract_date_parts(day.date)
            print(date['day'], RED_COLOR, '+' * day.max_temperature + BLACK_COLOR, str(day.max_temperature) + 'C')
            print(date['day'], BLUE_COLOR, '+' * day.min_temperature + BLACK_COLOR, str(day.min_temperature) + 'C')


# Draw combine horizontal bar graph on same line
def draw_combine_horizontal_bar_graph(path, date_string):
    month, year = extract_year_month(date_string)
    file_name = get_file_name(year, month)
    file_data = read_file(path, file_name)

    if file_data:
        date = extract_date_parts(file_data[0].date)
        print(date['month'], date['year'])

        for day in file_data:
            date = extract_date_parts(day.date)
            print(date['day'], BLUE_COLOR,
                  '+' * day.min_temperature + RED_COLOR + '+' * day.min_temperature + BLACK_COLOR,
                  str(day.min_temperature) + 'C' + " - " + str(day.max_temperature) + 'C')
