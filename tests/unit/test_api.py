from unittest import TestCase
import requests


class TestApi(TestCase):

    def setUp(self) -> None:
        self.api_end_point = "https://jsonplaceholder.typicode.com/todos"

        self.params = {"_start": str(45),
                       "_limit": str(1)}

        self.params_filters = {"completed": "false",
                               "_limit": str(10),
                               "_start": str(9)}

    def test_api_is_online(self):
        response = requests.get(self.api_end_point)
        assert (response.status_code == 200)

    def test_api_has_pagination(self):
        # Asking for https://jsonplaceholder.typicode.com/todos?completed=false&?_start=9&_limit=10
        response = requests.get(self.api_end_point, params=self.params_filters)
        assert (response.status_code == 200)
        assert (len(response.json()) == 10)


    def test_api_has_filters(self):
        # Asking for: "https://jsonplaceholder.typicode.com/todos?_start=45&_limit=1"
        response = requests.get(self.api_end_point, params=self.params)

        assert (response.status_code == 200)
        assert (response.json()[0]['userId'] == 3)
        assert (response.json()[0]['id'] == 46)
        assert (response.json()[0]['title'] == "vel voluptatem repellat nihil placeat corporis")
        assert (response.json()[0]['completed'] == False)


    def test_api_headers(self):
        # Asking for: "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(self.api_end_point)
        assert (response.headers['content-type'] == "application/json; charset=utf-8")
        assert (response.encoding == "utf-8")