from datetime import datetime
from calendar import month_abbr, month_name
import os

from constants import DATE_FORMAT, BLACK_COLOR, BLUE_COLOR, RED_COLOR


def get_weather_file_path(path, year, month):
    """
    Finds a weather file matching the specified year and month.
    
    Searches through files in the given directory path to find a file
    that contains both the year and the month abbreviation in its name.
    
    Args:
        path (str): The directory path to search for weather files.
        year (int): The year to search for in the filename.
        month (int): The month number (1-12) to search for in the filename.
    
    Returns:
        str | None: The full path to the matching file if found, None otherwise.
    """
    month_abbreviation = month_abbr[month]

    return next(
        (os.path.join(path, file_name) for file_name in os.listdir(path)
         if str(year) in file_name and month_abbreviation in file_name),
        None
    )
         


def extract_month_and_year(date_string):
    """
    Extracts month and year from a date string.
    
    Parses a date string in the format "YYYY/MM" and extracts the
    year and month as integers. Validates that the month is between 1 and 12.
    
    Args:
        date_string (str): A date string in the format "YYYY/MM".
    
    Returns:
        tuple[int, int]: A tuple containing (month, year) as integers.
    
    Raises:
        ValueError: If the month is not between 1 and 12.
    """
    parts = date_string.split("/")
    year = int(parts[0])
    month = int(parts[1])

    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")

    return month, year


def extract_date_parts(date_str):
    """
    Extracts day, month, and year components from a date string.
    
    Parses a date string using the DATE_FORMAT constant and returns
    a dictionary containing the day, month, and year components.
    
    Args:
        date_str (str): A date string in the format specified by DATE_FORMAT.
    
    Returns:
        dict: A dictionary with keys "day", "month", and "year" containing
            the respective integer values.
    """
    dt = datetime.strptime(date_str, DATE_FORMAT)
    return {
        "day": dt.day,
        "month": dt.month,
        "year": dt.year
    }


def find_max_weather_item(weather_items_list, weather_item_key):
    """
    Finds the weather item with the maximum value for a specified key.
    
    Searches through a list of weather items and returns the item that
    has the highest value for the specified weather item key.
    
    Args:
        weather_items_list (list): A list of weather item objects or dictionaries.
        weather_item_key (str): The key to compare values for (e.g., "max_temperature").
    
    Returns:
        object: The weather item with the maximum value for the specified key.
    """
    maximum_value = max(weather_items_list, key=lambda weather_item : weather_item[weather_item_key])

    return maximum_value


def find_min_weather_item(weather_items_list, weather_item_key):
    """
    Finds the weather item with the minimum value for a specified key.
    
    Searches through a list of weather items and returns the item that
    has the lowest value for the specified weather item key.
    
    Args:
        weather_items_list (list): A list of weather item objects or dictionaries.
        weather_item_key (str): The key to compare values for (e.g., "min_temperature").
    
    Returns:
        object: The weather item with the minimum value for the specified key.
    """
    minimum_value = min(weather_items_list, key=lambda weather_item : weather_item[weather_item_key])

    return minimum_value


def find_average_weather_item(month_data, weather_item_key):
    """
    Calculates the average value for a specified weather item key across month data.
    
    Computes the average of all non-empty values for the specified key
    across all days in the month data. Returns 0 if no data is available.
    
    Args:
        month_data (list): A list of weather item objects or dictionaries
            representing daily weather data for a month.
        weather_item_key (str): The key to calculate the average for
            (e.g., "max_temperature", "mean_humidity").
    
    Returns:
        int: The rounded average value for the specified weather item key.
    """
    values = [day[weather_item_key] for day in month_data if day[weather_item_key]]

    return round(sum(values) / len(values)) if values else 0
