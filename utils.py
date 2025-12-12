from file_data_parser import ParseFileData
from graph import BarGraph
from helpers import extract_month_and_year
from print_message import PrintMessages
from weather_file_manager import WeatherFileManager

 
def handle_month_graph_generation(parsed_month_data, month, year, combine_graph=False):
    """
    Generates and displays a bar graph for a month's weather data.

        combine_graph (bool, optional): If True, displays a combined graph
            showing both max and min temperatures. If False, displays separate
            graphs for max and min temperatures. Defaults to False.
    
    Returns:
        None: This function prints output directly and does not return a value.
    """
    BarGraph.display_graph_header(month, year)
    BarGraph.display_combined_horizontal_graph(parsed_month_data) if combine_graph else BarGraph.display_separated_horizontal_graph(parsed_month_data)            
