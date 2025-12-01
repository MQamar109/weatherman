from datetime import datetime
from constants import MAX_TEMPERATURE,MIN_TEMPERATURE,DATE,RED_COLOR,BLUE_COLOR,BLACK_COLOR,MONTH_NUMBER


#create file ame with year and month
def get_file_name(year,month):
    return f"Murree_weather_{year}_{MONTH_NUMBER[month]}.txt"

#Extract month and year
def extract_year_month(date_string):
    parts = date_string.split('/')
    year = int(parts[0])
    month = int(parts[1])
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")
    return month, year

#Get date format like 24 March 2025
def extract_date_parts(date_str):
    dt = datetime.strptime(date_str, '%Y-%m-%d')

    return {
        'day': dt.day,
        'month': dt.strftime('%B'),
        'year': dt.year
    }


# Find Highest value of any entity
def find_entity_highest_value(month_data, entity):
    highest_value = int(month_data[0][entity])
    date = month_data[0][DATE]
    for record in month_data:
        if record[entity]:
            if int(record[entity]) > highest_value:
                highest_value = int(record[entity])
                date = record[DATE]

    return {'value':highest_value, **extract_date_parts(date)}

# Find lowest value of any entity
def find_entity_lowest_value(month_data, entity):
    lowest_value = int(month_data[0][entity])
    date = month_data[0][DATE]
    for record in month_data:
        if record[entity]:
            if int(record[entity]) < lowest_value:
                date=record[DATE]
                lowest_value= int(record[entity])

    return {'value':lowest_value, **extract_date_parts(date)}

# Find average value of any entity
def find_average_entity_value(month_data, entity):
    total_value=0
    for day in month_data:
        if day[entity]:
            total_value+=int(day[entity])

    average_value=total_value/len(month_data)
    return average_value

#print horizontal bar chart of a month on 2 lines
def draw_horizontal_bar_chart_separate_lines(month_data):
    date=extract_date_parts(month_data[0][DATE])
    print(date['month'],date['year'])

    for day in month_data:
        date=extract_date_parts(day[DATE])
        print(date['day'] ,RED_COLOR, '+' * (int(day[MAX_TEMPERATURE] or 0)) + BLACK_COLOR, (day[MAX_TEMPERATURE] or '0') + 'C')
        print(date['day'] ,BLUE_COLOR,  '+' * (int(day[MIN_TEMPERATURE] or 0)) + BLACK_COLOR, (day[MIN_TEMPERATURE] or '0') + 'C')

#print horizontal bar chart of a month on single line
def draw_horizontal_bar_chart_single_line(month_data):
    date=extract_date_parts(month_data[0][DATE])
    print(date['month'],date['year'])

    for day in month_data:
        date = extract_date_parts(day[DATE])
        print(date['day'],BLUE_COLOR, '+' * (int(day[MIN_TEMPERATURE] or 0)) + RED_COLOR, '+' * (int(day[MAX_TEMPERATURE] or 0)) + BLACK_COLOR,(day[MIN_TEMPERATURE] or '0')+ 'C' + " - " +(day[MAX_TEMPERATURE] or '0') + 'C')
