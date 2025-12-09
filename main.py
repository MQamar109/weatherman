from itertools import chain
import parser

from file_data_parser import ParseFileData
from helpers import extract_month_and_year
from print_message import PrintMessages
from utils import handle_month_graph_generation
from weather_calculation import WeatherCalculation
from weather_file_manager import WeatherFileManager


if __name__ == '__main__':
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

        month_statistics = {"month_avg": args.month,
                            "separate_graph": args.graph,
                            "combine_graph" : args.combine_graph}

        for month_key, month_agrs in month_statistics.items():
            if month_agrs:
                month, year = extract_month_and_year(month_agrs)
                month_file_data = WeatherFileManager.fetch_monthly_weather_file_data(
                    args.path, month, year
                    )
                parsed_month_data = ParseFileData.parse_to_weather_items(month_file_data) if month_file_data else []

                if parsed_month_data:
                    if month_key == "month_avg":
                        monthly_calculation_result = WeatherCalculation.calculate_monthly_temperature_and_humidity_average(
                        parsed_month_data)
                        print(monthly_calculation_result)

                    if month_key == "separate_graph":
                        handle_month_graph_generation(parsed_month_data, month, year)

                    if month_key == "combine_graph":
                        handle_month_graph_generation(parsed_month_data, month, year, combine_graph=True)
                else:
                    PrintMessages.monthly_weather_data_not_found(month, year)
