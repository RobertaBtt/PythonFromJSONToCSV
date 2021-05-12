from unittest import TestCase
from tempfile import TemporaryFile


class TestFile(TestCase):

    def setUp(self) -> None:
        self.name_file = "2021_05_12_999.csv"
        self.header_csv = "userId, id,title,completed"

    def test_file_has_been_created(self):
        # Temporary text file in write mode
        temp_file = TemporaryFile('w+t')
        temp_file.write(self.header_csv)

        # Begin of the file
        temp_file.seek(0)
        data = temp_file.read()
        temp_file.close()
        assert (data == self.header_csv)