class PrintMessages:
    """
    A class for printing messages to the console.
    
    This class provides methods to print messages when no data is found
    for a specific month or year.
    """
    @staticmethod
    def monthly_weather_data_not_found(month, year):
        print(f"No data found  of this month: {month}, {year}")

    @staticmethod
    def yearly_weather_data_not_found(year):
        print(f"No data found of this year {year}")
