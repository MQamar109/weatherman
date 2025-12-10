from constants import (
    PKT_DATE,
    PKST_DATE,
    MAX_HUMIDITY,
    MAX_TEMPERATURE,
    MEAN_HUMIDITY,
    MIN_TEMPERATURE,
)
from weather_containers import WeatherItem


class ParseFileData:
    """
    A class for parsing raw weather file data into structured WeatherItem objects.
    
    This class provides methods to validate and convert weather data from CSV files
    (represented as dictionaries) into WeatherItem instances, handling missing or
    invalid values appropriately.
    """
    @classmethod
    def parse_weather_value(cls, weather_value):
        return int(weather_value) if weather_value not in ("", " ", None,) else 0

    @classmethod
    def parse_to_weather_items(cls, weather_file_data):
        weather_items = []

        for row in weather_file_data:
            weather_item = WeatherItem(
                date=row.get(PKT_DATE) or row.get(PKST_DATE),
                max_temp=cls.parse_weather_value(row.get(MAX_TEMPERATURE)),
                min_temp=cls.parse_weather_value(row.get(MIN_TEMPERATURE)),
                mean_humidity=cls.parse_weather_value(row.get(MEAN_HUMIDITY)),
                max_humidity=cls.parse_weather_value(row.get(MAX_HUMIDITY))
            )
            weather_items.append(weather_item)

        return weather_items
