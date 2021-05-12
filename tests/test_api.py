from unittest import TestCase
import requests

class TestApi(TestCase):

    def setUp(self) -> None:
        self.api_end_point = "https://jsonplaceholder.typicode.com/todos"
        self.params = {"_start": str(45), "_limit": str(1)}

    def test_api_is_online(self):
        response =  requests.get(self.api_end_point)
        assert (response.status_code == 200)

    def test_api_has_pagination(self):

        # Asking for:
        response = requests.get(self.api_end_point, params=self.params)

        assert (response.status_code == 200)
        assert (response.json()[0]['userId'] == 3)
        assert (response.json()[0]['id'] == 46)
        assert (response.json()[0]['title'] == "vel voluptatem repellat nihil placeat corporis")
        assert (response.json()[0]['completed'] == False)

