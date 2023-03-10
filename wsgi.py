import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/api"))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/db"))
from api.water_level import WaterLevelController
from api.status import StatusController
from datetime import datetime
from db.connection import Connection


def application(environ, start_response):
    path = environ['PATH_INFO']
    status = '200 OK'
    params = {}

    if 'QUERY_STRING' in environ and str(environ['QUERY_STRING']) != "":
        query_list = str(environ['QUERY_STRING']).split("&")
        for item in query_list:
            param = item.split("=")
            params.update({param[0]: param[1]})


    if path == '/api/water-level':
        controller = WaterLevelController(params)
        output = controller.response().encode('utf-8')
        return [output]
    if path == '/api/status':
        controller = StatusController()
        output = controller.response().encode('utf-8')
        return [output]

    status = '404 Not Found'
    # response_headers = [('Content-type', 'text/plain'),
    #                     ('Content-Length', str(len(output)))]
    # start_response(status, response_headers)
    return [b'404 Page Not Found']


if __name__ == '__main__':
    environ1 = {'PATH_INFO': '/api/water-level',
               'REQUEST_METHOD': 'GET',
               'QUERY_STRING': 'level=85'}
    environ2 = {'PATH_INFO': '/api/status',
               'REQUEST_METHOD': 'GET',
               'QUERY_STRING': ''}
    environ3 = {'PATH_INFO': '/web/dashboard',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': 'user=1'}
    environ4 = {'PATH_INFO': '/web/login',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': ''}
    environ5 = {'PATH_INFO': '/web/register',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': ''}
    output = application(environ2, None)
    print(output[0])
    # print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    # Connection().initialize()
