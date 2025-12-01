from file_handling import read_file
from constants import MAX_TEMPERATURE,MIN_TEMPERATURE,MAX_HUMIDITY,MEAN_HUMIDITY
from helpers import find_entity_lowest_value,find_entity_highest_value,draw_horizontal_bar_chart_separate_lines,get_file_name,find_average_entity_value,draw_horizontal_bar_chart_single_line,extract_year_month


#Find the highest and lowest temperature and most humidity
def find_year_highest_temp_humidity_and_lowest_temp(year_data):
    first_month = year_data[0]
    highest_temp = find_entity_highest_value(first_month,MAX_TEMPERATURE)
    lowest_temp = find_entity_lowest_value(first_month,MIN_TEMPERATURE)
    highest_humidity = find_entity_highest_value(first_month,MAX_HUMIDITY)

    for month in year_data[1:]:
        high_temperature = find_entity_highest_value(month, MAX_TEMPERATURE)
        if high_temperature['value'] > highest_temp['value']:
            highest_temp=high_temperature

        low_temperature=find_entity_lowest_value(month,MIN_TEMPERATURE)
        if low_temperature['value'] < lowest_temp['value']:
            lowest_temp=low_temperature

        high_humidity = find_entity_highest_value(month, MAX_HUMIDITY)
        if high_humidity['value'] > highest_humidity['value']:
            highest_humidity = high_humidity

    return {'highest_temp':highest_temp,'lowest_temp':lowest_temp, 'highest_humidity':highest_humidity}

def calculate_month_averages(path,date_string):
    month, year=extract_year_month(date_string)
    file_name=get_file_name(year,month)
    file_data=read_file(path,file_name)
    if file_data:
        avg_highest_temperature = find_average_entity_value(file_data, MAX_TEMPERATURE)
        avg_lowest_temperature = find_average_entity_value(file_data, MIN_TEMPERATURE)
        avg_mean_humidity = find_average_entity_value(file_data, MEAN_HUMIDITY)
        print(f'Highest Average: {avg_highest_temperature}C')
        print(f'Lowest Average: {avg_lowest_temperature}C')
        print(f'Average Mean Humidity: {avg_mean_humidity}%')


def get_year_calculations_and_date(path,year):
    year_data=[]
    for month in range(12):
        file_name=get_file_name(year,month+1)
        file_data=read_file(path,file_name)
        if file_data:
            year_data.append(file_data)
    if year_data:
        data=find_year_highest_temp_humidity_and_lowest_temp(year_data)
        high_temp, low_temp, high_humidity = data['highest_temp'], data['lowest_temp'], data['highest_humidity']
        print(f'Highest: {high_temp['value']}C on {high_temp['month']} {high_temp['day']}')
        print(f'Lowest: {low_temp['value']}C on {low_temp['month']} {low_temp['day']}')
        print(f'Humidity: {high_humidity['value']}% on {high_humidity['month']} {high_humidity['day']}')
    else:
        print('Not any File of this year found!')

def print_graph_separate_lines(path,date_string):
    month, year=extract_year_month(date_string)
    file_name=get_file_name(year,month)
    file_data=read_file(path,file_name)

    if file_data:
        draw_horizontal_bar_chart_separate_lines(file_data)


def print_graph_single_line(path, date_string):
    month, year=extract_year_month(date_string)
    file_name = get_file_name(year, month)
    file_data = read_file(path, file_name)

    if file_data:
        draw_horizontal_bar_chart_single_line(file_data)
