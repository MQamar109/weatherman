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
    @classmethod
    def validate_weather_value(cls, value):
        return int(value) if value not in ('', ' ', None,) else 0

    @classmethod
    def parse_to_weather_items(cls, file_data):
        weather_items = []
        for row in file_data:
            weather_item = WeatherItem(
                date=row.get(PKT_DATE) or row.get(PKST_DATE),
                max_temp=cls.validate_weather_value(row.get(MAX_TEMPERATURE)),
                min_temp=cls.validate_weather_value(row.get(MIN_TEMPERATURE)),
                mean_humidity=cls.validate_weather_value(row.get(MEAN_HUMIDITY)),
                max_humidity=cls.validate_weather_value(row.get(MAX_HUMIDITY))
            )
            weather_items.append(weather_item)

        return weather_items
