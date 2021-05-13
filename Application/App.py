from Services.ApiService import ApiService
from Application import Configuration
from Services import ServiceAdapter as s

class App:
    def __init__(self, service_type):
        self._service = s.ServiceAdapter().get_service(service_type)()

    def get_application_service(self) -> ApiService:
        return self._service
