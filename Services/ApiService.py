from sys import stderr
import requests
import pathlib
import csv
from datetime import datetime


class ApiService:


    def run(self):
        print('Running ApiService', file=stderr)

    def get_all(self, **params):

        try:
            response = requests.get(params['end_point'], params=params['api_params'])
            return response
        except Exception as ex:
            print(ex)

    # Single Responsibility Principle
    def save_to_files(self, response):
        path = pathlib.Path().absolute()
        file_name = str(path) + "/storage/" + datetime.today().strftime('%Y_%m_%d')

        for element in response.json():
            todo_id = element['id']
            file_path = file_name + "_" + str(todo_id) + ".csv"

            with open(file_path, mode='w+', newline="\n") as todo_file:
                csv.writer(todo_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                fieldnames = ['userId', 'id', 'title', 'completed']
                writer = csv.DictWriter(todo_file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow(element)


