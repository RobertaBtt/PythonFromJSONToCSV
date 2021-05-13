from sys import stderr
import requests


class ApiService:


    def run(self):
        print('Running ApiService', file=stderr)


    def get_all(self, **params):
        try:
            response = requests.get(params['end_point'], params=params['api_params'])
            return response
        except Exception as ex:
            print(ex)
