from Services import ApiService
from Services import DBService
import logging
logger = logging.getLogger('Roby')

#This class can be viewd as an AbstractFactory
# for the adapters, because the data source
# can be different

# Registry / Service container of the Classes that
# can adapt to different data sources or services (could be database, API, FTP, Bucket S3 etc etc)
# Using the Python decorators


SERVICE_ADAPTERS = dict()


def register():
    """Register a Service Class that can adapt to different data sources"""
    SERVICE_ADAPTERS["API"] = ApiService.ApiService
    SERVICE_ADAPTERS["DB"] = DBService.DbService


class ServiceAdapter:

    def __init__(self):
        register()

    def get_service(self, service_type):
        return SERVICE_ADAPTERS[service_type]
