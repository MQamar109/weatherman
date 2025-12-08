from file_data_parser import ParseFileData
from graph import BarGraph
from helpers import extract_month_and_year
from print_message import PrintMessages
from weather_file_manager import WeatherFileManager

 
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
    month_file_data = WeatherFileManager.fetch_monthly_weather_file_data(path, month, year)
    parsed_month_data = ParseFileData.parse_to_weather_items(month_file_data) if month_file_data else []
    
    if parsed_month_data:
        BarGraph.display_graph_header(month, year)
        BarGraph.display_combine_horizontal_graph(parsed_month_data) if combine_graph else BarGraph.display_separated_horizontal_graph(parsed_month_data)            
    else:
        PrintMessages.monthly_weather_data_not_found(month, year)
