import csv
import os

class FileHandling:
    """
    A class for handling file operations.
    
    This class provides methods to check if a file exists and read
    CSV data from a file.
    """
    @classmethod
    def weather_file_exists(cls, weather_file_path):
        return os.path.exists(weather_file_path)

    @classmethod
    def read_csv_file(cls, weather_file_path):
        csv_weather_file_data = []

        if cls.weather_file_exists(weather_file_path):
            with open(weather_file_path, 'r', newline='') as file:
                weather_file_data = csv.DictReader(file)
                weather_file_data.fieldnames = [fieldname.strip() for fieldname in weather_file_data.fieldnames]
                for row in weather_file_data:
                    csv_weather_file_data.append(row)
                    
        return csv_weather_file_data
