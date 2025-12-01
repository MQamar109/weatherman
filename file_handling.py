import csv
import os

def read_file(path,file_name):
    file_path=os.path.join(path,file_name)
    csv_file_data=[]
    if os.path.exists(file_path):
        with open(file_path,'r',newline='') as file:
            data=csv.DictReader(file)
            for row in data:
                csv_file_data.append(row)
    else:
        print(f'File does not exist {file_path}')
    return csv_file_data