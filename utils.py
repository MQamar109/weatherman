from file_data_parser import ParseFileData
from graph import BarGraph
from helpers import extract_month_and_year
from print_message import PrintMessages
from weather_file_manager import WeatherFileManager

def handle_month_file_read_and_parse(path, month, year):
    """
    Reads and parses weather data for a specific month and year.
    
    Fetches the weather file for the given month and year, then parses
    the raw CSV data into structured WeatherItem objects.
    
    Args:
        path (str): The directory path where weather files are stored.
        month (int): The month number (1-12).
        year (int): The year to fetch data for.
    
    Returns:
        list[WeatherItem]: A list of WeatherItem objects containing parsed
            weather data for each day of the month. Returns an empty list
            if the file is not found or contains no data.
    """
    month_file_data = WeatherFileManager.fetch_month_weather_file_data(path, month, year)
    return ParseFileData.parse_to_weather_items(month_file_data) if month_file_data else []

 
def handle_month_graph_generation(path, date_string, combine_graph=False):
    """
    Generates and displays a bar graph for a month's weather data.
    
    Reads weather data for the specified month and year (extracted from
    the date string), then generates either a combined or separate
    horizontal bar graph showing temperature data. Displays an error
    message if no data is found for the month.
    
    Args:
        path (str): The directory path where weather files are stored.
        date_string (str): A date string in the format "YYYY/MM" from which
            the month and year will be extracted.
        combine_graph (bool, optional): If True, displays a combined graph
            showing both max and min temperatures. If False, displays separate
            graphs for max and min temperatures. Defaults to False.
    
    Returns:
        None: This function prints output directly and does not return a value.
    """
    month, year = extract_month_and_year(date_string)
    parsed_month_data = handle_month_file_read_and_parse(path, month, year)
    if parsed_month_data:
        BarGraph.print_graph_header(month, year)
        if combine_graph:
            BarGraph.combine_horizontal_graph(parsed_month_data)
        else:
            BarGraph.separate_horizontal_graph(parsed_month_data)            
    else:
        PrintMessages.month_data_not_found(month, year)
