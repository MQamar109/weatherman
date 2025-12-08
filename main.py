from itertools import chain
import parser

from file_data_parser import ParseFileData
from helpers import extract_month_and_year
from print_message import PrintMessages
from utils import handle_month_file_read_and_parse, handle_month_graph_generation
from weather_calculation import WeatherCalculation
from weather_file_manager import WeatherFileManager


if __name__ == '__main__':
    args = parser.get_parser()
    if args.year:
        yearly_files_readings = WeatherFileManager.fetch_yearly_weather_files_data(args.path, args.year)

        if yearly_files_readings:
            year_flat_data = chain.from_iterable(yearly_files_readings)
            parsed_year_data = ParseFileData.parse_to_weather_items(year_flat_data)
            year_calculation_result = WeatherCalculation.calculate_yearly_temperature_and_humidity_statistics(parsed_year_data)

            if year_calculation_result:
                print(year_calculation_result)
        else:
            PrintMessages.yearly_weather_data_not_found(args.year)

    if args.month:
        month, year = extract_month_and_year(args.month)
        parsed_month_data = handle_month_file_read_and_parse(args.path, month, year)
        if parsed_month_data:
            result = WeatherCalculation.calculate_month_temperature_and_humidity_average(parsed_month_data)
            if result:
                print(result)
        else:
            PrintMessages.monthly_weather_data_not_found(month, year)

    if args.graph:
        handle_month_graph_generation(args.path, args.graph)
       
    if args.combine_graph:
        handle_month_graph_generation(args.path, args.combine_graph, combine_graph=True)
