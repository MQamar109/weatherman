from itertools import chain
import parser

from file_data_parser import ParseFileData
from helpers import extract_month_and_year
from print_message import PrintMessages
from utils import handle_month_graph_generation
from weather_calculation import WeatherCalculation
from weather_file_manager import WeatherFileManager


if __name__ == "__main__":
    args = parser.get_parser()
    if args.year:
        yearly_files_readings = WeatherFileManager.fetch_yearly_weather_files_data(
            args.path, args.year
            )

        if yearly_files_readings:
            year_flat_data = chain.from_iterable(yearly_files_readings)
            parsed_year_data = ParseFileData.parse_to_weather_items(year_flat_data)
            year_calculation_result = WeatherCalculation.calculate_yearly_temperature_and_humidity_statistics(
                parsed_year_data
                )

            if year_calculation_result:
                print(year_calculation_result)
        else:
            PrintMessages.yearly_weather_data_not_found(args.year)

    if args.month or args.graph or args.combine_graph:

        month_arguments = {"month_avg": args.month,
                            "separate_graph": args.graph,
                            "combine_graph" : args.combine_graph}

        for month_stat_key, month_stat_agr in month_arguments.items():
            if month_stat_agr:
                month, year = extract_month_and_year(month_stat_agr)
                month_file_data = WeatherFileManager.fetch_monthly_weather_file_data(
                    args.path, month, year
                    )
                parsed_month_data = ParseFileData.parse_to_weather_items(month_file_data) if month_file_data else []

                if parsed_month_data:

                    month_statistics_actions = {
                        "month_avg": lambda parsed_data: print(
                            WeatherCalculation.calculate_monthly_temperature_and_humidity_average(
                                parsed_data)),
                        "separate_graph": lambda parsed_data : handle_month_graph_generation(
                            parsed_data, month, year),
                        "combine_graph": lambda parsed_data : handle_month_graph_generation(
                            parsed_data, month, year, combine_graph=True)}

                    month_statistics_actions[month_stat_key](parsed_month_data)
                else:
                    PrintMessages.monthly_weather_data_not_found(month, year)
