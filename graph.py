from calendar import month_name

from constants import BLACK_COLOR, BLUE_COLOR, RED_COLOR


class BarGraph:
    """
    A class for generating and displaying bar graphs for weather data.
    
    This class provides methods to print graph headers, generate combined
    or separate horizontal bar graphs, and format temperature data for display.
    """
    @staticmethod
    def display_graph_header(month, year):
        print(f"{month_name[month]} {year}")

    @staticmethod
    def display_combined_horizontal_graph(monthly_weather_data):
        for day in monthly_weather_data:
            print(day.get_day(), BLUE_COLOR,
                  "+" * day.min_temperature + RED_COLOR + "+" * 
                  day.min_temperature + BLACK_COLOR, str(day.min_temperature)
                   + "C" + " - " + str(day.max_temperature) + "C")

    @staticmethod
    def display_separated_horizontal_graph(monthly_weather_data):
        for day in monthly_weather_data:
            print(day.get_day(), RED_COLOR,
                  "+" * day.max_temperature + BLACK_COLOR,
                  str(day.max_temperature) + "C")
            print(day.get_day(), BLUE_COLOR,
                  "+" * day.min_temperature + BLACK_COLOR,
                  str(day.min_temperature) + "C")
