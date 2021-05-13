from unittest import TestCase
from tempfile import TemporaryFile
import pathlib
from datetime import datetime

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


    def test_file_is_created_in_storage(self):

        path = pathlib.Path().absolute()
        file_name = str(path) + "/storage/" + datetime.today().strftime('%Y_%m_%d')

        todo_id = 1323
        file_path = file_name + "_" + str(todo_id) + ".csv"

        with open(file_path, mode='w+') as todo_file:
            todo_file.write(self.header_csv + "\n")
            todo_file.write("test, test, test, test")
            todo_file.seek(0)

            first_line = todo_file.readline()
            second_line = todo_file.readline()

            assert (first_line == self.header_csv+"\n")
            assert (second_line == "test, test, test, test")

            todo_file.close
