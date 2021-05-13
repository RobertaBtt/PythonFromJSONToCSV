from unittest import TestCase
from Services import ServiceAdapter as s
from datetime import datetime
import pathlib

class TestService(TestCase):

    def setUp(self) -> None:
        self.api_end_point = "https://jsonplaceholder.typicode.com/todos"
        self.type = "API"
        self.header_csv = "userId,id,title,completed"

    def test_two_todos_are_saved_in_file(self):

        # Asking for https://jsonplaceholder.typicode.com/todos?_start=1&_limit=2
        api_params = {"completed": "false",
                          "_start": str(1),
                          "_limit": str(2)}

        path = pathlib.Path().absolute()

        params = {}
        params['end_point'] = self.api_end_point
        params['api_params'] = api_params

        service = s.ServiceAdapter().get_service(self.type)

        result = service().get_all(**params)
        service().save_to_files(result)

        assert (result.status_code == 200)
        assert (result.json()[0]['userId'] == 1)
        assert (result.json()[0]['id'] == 2)
        assert (result.json()[0]['title'] == "quis ut nam facilis et officia qui")
        assert (result.json()[0]['completed'] == False)

        file_name = str(path) + "/storage/" + datetime.today().strftime('%Y_%m_%d')
        file_path = file_name + "_" + str(result.json()[0]['id']) + ".csv"

        with open(file_path, mode='r') as todo_file:
            first_line = todo_file.readline()
            second_line = todo_file.readline()

            assert (first_line == self.header_csv + "\n")
            assert (second_line == "1,2,quis ut nam facilis et officia qui,False"+"\n")

            todo_file.close


