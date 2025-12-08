import csv
import os

class FileHandling:
    @classmethod
    def is_file_exist(cls, file_path):
        return os.path.exists(file_path)

    @classmethod
    def read_csv_file(cls, file_name):
        csv_file_data = []

        if cls.is_file_exist(file_name):
            with open(file_name, 'r', newline='') as file:
                file_data = csv.DictReader(file)
                file_data.fieldnames = [name.strip() for name in file_data.fieldnames]
                for row in file_data:
                    csv_file_data.append(row)
        return csv_file_data

