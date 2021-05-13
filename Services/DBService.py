from sys import stderr

class DbService:
    def __init__(self):
        pass

    def run(self):
        print('Running DbService', file=stderr)

    def get_all(self, **params):
        raise  NotImplementedError

    def save_to_files(self, response):
        raise NotImplementedError