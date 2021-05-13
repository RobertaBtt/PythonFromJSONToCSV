# It acts as a configurator file

CONF = {}

CONF['end_point'] = "https://jsonplaceholder.typicode.com/todos"
CONF['type'] = "API"
API_PARAMS = {"completed": "false",
              "_start": str(1),
              "_limit": str(0)}

CONF['api_params'] = API_PARAMS
