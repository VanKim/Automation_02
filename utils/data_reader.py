import csv
import json


class DataReader:
    @staticmethod
    def read_data_from_csv_file(file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            keywords = []
            for row in csv_reader:
                keywords.append(row['keyword'])
            return keywords

    @staticmethod
    def read_data_from_json_file(file_path):
        with open(file_path, mode='r') as file:
            json_reader = json.load(file)
        return json_reader
