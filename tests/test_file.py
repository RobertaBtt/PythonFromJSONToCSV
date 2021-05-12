from unittest import TestCase
from tempfile import TemporaryFile


class TestFile(TestCase):

    def setUp(self) -> None:
        self.name_file = "2021_05_12_999.csv"
        self.header_csv = "userId, id,title,completed"
        self.content_test = "1,1,delectus aut autem,false"

    def test_file_created_just_header(self):
        # Temporary text file in write mode
        with TemporaryFile('w+t') as temp_file:
            temp_file.write(self.header_csv)

            # Begin of the file
            temp_file.seek(0)
            data = temp_file.read()
            temp_file.close()
            assert (data == self.header_csv)

    def test_file_created_header_and_content(self):
        # Temporary text file in write mvode
        with TemporaryFile('w+t') as temp_file:

            temp_file.write(self.header_csv +"\n")
            temp_file.write(self.content_test)

            # Begin of the file
            temp_file.seek(0)

            first_line = temp_file.readline()
            second_line = temp_file.readline()
            temp_file.close()

            assert (first_line == self.header_csv+"\n")
            assert (second_line == self.content_test)
