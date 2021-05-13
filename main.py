#!/usr/bin/env python

from Application.App import App
from Application import Configuration

# Important change: we setup externally the configuration of
# which service we are going to use

service_type = Configuration.CONF['type']

app = App(service_type)
service = app.get_application_service

# Just to show which Service is running
service().run()

response = service().get_all(**Configuration.CONF)
service().save_to_files(response)