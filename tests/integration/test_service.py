from unittest import TestCase
from Services import ServiceAdapter as s


class TestService(TestCase):

    def setUp(self) -> None:
        self.api_end_point = "https://jsonplaceholder.typicode.com/todos"
        self.type = "API"

    def test_todo_is_saved_in_file(self):

        params = {"completed": "false",
                          "_start": str(1),
                          "_limit": str(1)}

        service = s.ServiceAdapter().get_adapter(self.type)
        result = service().get_all(**params)

        assert (result == "ok")