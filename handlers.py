from file_handling import read_file
from helpers import (
    extract_date_parts,
    extract_month_and_year,
    find_average_value,
    find_highest_value,
    find_lowest_value,
    draw_separate_bar_graph,
    draw_combine_bar_graph,
    get_file_name,
    fetch_file_data,
    fetch_month_file_data,
    fetch_year_files_data,
    print_graph_header
)
from weather_containers import MonthlyAveragesResult, YearlyCalculation


#Calculate month data (averages of max, min temperature and mean humidity
def calculate_month_averages(path, date_string):
    month_data = fetch_month_file_data(path, date_string)

    if month_data:
        avg_highest_temperature = find_average_value(month_data, 'max_temperature')
        avg_lowest_temperature = find_average_value(month_data, 'min_temperature')
        avg_mean_humidity = find_average_value(month_data, 'mean_humidity')
        averages = MonthlyAveragesResult(avg_max_temp=avg_highest_temperature,
                                         avg_min_temp=avg_lowest_temperature,
                                         avg_mean_humidity=avg_mean_humidity)
        return averages


def print_month_average_results(path, date_string):
    result = calculate_month_averages(path, date_string)
    if result:
        print(result)
    else:
        print("No data of this month found.")


def print_combine_graph(path, date_string):
    month_data = fetch_month_file_data(path, date_string)
    if month_data:
        print_graph_header(date_string)
        draw_combine_bar_graph(month_data)


def print_separate_graph(path, date_string):
    month_data = fetch_month_file_data(path, date_string)
    if month_data:
        print_graph_header(date_string)
        draw_separate_bar_graph(month_data)


def find_year_extreme(year_data, key, find_max=True):
    extreme = find_highest_value(year_data[0], key) if find_max else find_lowest_value(year_data[0], key)

    for month in year_data[1:]:
        if find_max:
            current_high = find_highest_value(month, key)
            if find_max and current_high['value'] > extreme['value']:
                extreme = current_high
        else:
            current_low = find_lowest_value(month, key)
            if current_low['value'] < extreme['value']:
                extreme = current_low

    return extreme


# Find the highest and lowest temperature and most humidity
def find_year_highest_temp_humidity_and_lowest_temp(year_data):
    highest_temp = find_year_extreme(year_data, 'max_temperature')
    lowest_temp = find_year_extreme(year_data, 'min_temperature', find_max=False)
    highest_humidity = find_year_extreme(year_data, 'max_humidity')

    return {'highest_temp': highest_temp,
            'lowest_temp': lowest_temp,
            'highest_humidity': highest_humidity}


def calculate_year_values(path, year):
    year_data = fetch_year_files_data(path, year)

    if year_data:
        data = find_year_highest_temp_humidity_and_lowest_temp(year_data)
        max_temp, min_temp, max_humidity = (data['highest_temp'],
                                        data['lowest_temp'],
                                        data['highest_humidity'])

        return YearlyCalculation(highest_temp=max_temp['value'],
                                 highest_temp_date={'day': max_temp['day'], 'month': max_temp['month']},

                                 lowest_temp=min_temp['value'],
                                 lowest_temp_date={'day': min_temp['day'], 'month': min_temp['month']},

                                 highest_humidity=max_humidity['value'],
                                 highest_humidity_date={'day': max_humidity['day'],'month': max_humidity['month']})


def print_year_result(path, year):
    result = calculate_year_values(path, year)
    if result:
        print(result)
    else:
        print("No data of this year found.")