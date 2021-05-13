from unittest import TestCase
from Services import ServiceAdapter as s
import pathlib

class TestService(TestCase):

    def setUp(self) -> None:
        self.api_end_point = "https://jsonplaceholder.typicode.com/todos"
        self.type = "API"

    def test_one_todo_is_saved_in_file(self):

        # Asking for https://jsonplaceholder.typicode.com/todos?_start=1&_limit=1
        api_params = {"completed": "false",
                          "_start": str(1),
                          "_limit": str(2)}

        params = {}
        params['end_point'] = self.api_end_point
        params['api_params'] = api_params

        service = s.ServiceAdapter().get_adapter(self.type)

        result = service().get_all(**params)
        service().save_to_files(result)

        assert (result.status_code == 200)
        assert (result.json()[0]['userId'] == 1)
        assert (result.json()[0]['id'] == 2)
        assert (result.json()[0]['title'] == "quis ut nam facilis et officia qui")
        assert (result.json()[0]['completed'] == False)


