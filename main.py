import parser
from itertools import chain

from file_data_parser import ParseFileData
from graph import BarGraph
from helpers import extract_month_and_year
from print_message import PrintMessages
from utils import handle_month_file_read_and_parse
from weather_file_manager import WeatherFileManager
from weather_calculation import WeatherCalculation

if __name__ == '__main__':
    args = parser.get_parser()
    if args.year:
        year_files_data = WeatherFileManager.fetch_year_files_data(args.path, args.year)

        if year_files_data:
            year_flat_data = chain.from_iterable(year_files_data)
            parsed_year_data = ParseFileData.parse_to_weather_items(year_flat_data)
            year_calculation_result = WeatherCalculation.calculate_yearly_temperature_and_humidity_statistics(parsed_year_data)

            if year_calculation_result:
                print(year_calculation_result)
        else:
            PrintMessages.year_data_not_found(args.year)

    if args.month:
        month, year = extract_month_and_year(args.month)
        parsed_month_data = handle_month_file_read_and_parse(args.path, month, year)
        if parsed_month_data:
            result = WeatherCalculation.calculate_month_temperature_and_humidity_average(parsed_month_data)
            if result:
                print(result)
        else:
            PrintMessages.year_data_not_found(month)

    if args.graph:
        month, year = extract_month_and_year(args.graph)
        parsed_month_data = handle_month_file_read_and_parse(args.path, month, year)
        if parsed_month_data:
            BarGraph.print_graph_header(month, year)
            BarGraph.separate_horizontal_graph(parsed_month_data)
        else:
            PrintMessages.year_data_not_found(month)

    if args.combine_graph:
        month, year = extract_month_and_year(args.combine_graph)
        parsed_month_data = handle_month_file_read_and_parse(args.path, month, year)
        if parsed_month_data:
            BarGraph.print_graph_header(month, year)
            BarGraph.combine_horizontal_graph(parsed_month_data)
        else:
            PrintMessages.year_data_not_found(month)
