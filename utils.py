from weather_file_manager import WeatherFileManager
from file_data_parser import ParseFileData


def handle_month_file_read_and_parse(path, month, year):
    month_file_data = WeatherFileManager.fetch_file_data(path, month, year)
    return ParseFileData.parse_to_weather_items(month_file_data) if month_file_data else []
