import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/api"))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/db"))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/web"))
from api.water_level import WaterLevelController
from api.status import StatusController
from api.switch import SwitchController
from api.auth import AuthController
from web.dashboard import DashboardController
from web.login import LoginController
from datetime import datetime
from db.connection import Connection


def start_response(a, b):
    pass


def api_water_level(params):
    if 'level' in params and 'user' in params:
        controller = WaterLevelController(params)
        output = controller.response().encode('utf-8')
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
    else:
        output = b'Incorrect Parameters'
        status = '400 Bad Request'
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
    return output, response_headers, status


def api_status(params):
    if 'user' in params:
        controller = StatusController(params)
        output = controller.response().encode('utf-8')
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
    else:
        output = b'Incorrect Parameters'
        status = '400 Bad Request'
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
    return output, response_headers, status


def web_dashboard(path):
    # try:
    user = int(path.rsplit("/", 1)[-1])
    controller = DashboardController(user)
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    # except:
    #     output = b'404 Not Found'
    #     status = '404 Not Found'
    #     response_headers = [('Content-type', 'text/plain'),
    #                         ('Content-Length', str(len(output)))]
    return output, response_headers, status


def api_on(path):
    user = int(path.rsplit("/", 1)[-1])
    SwitchController(1, user)
    output = b''
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def api_off(path):
    user = int(path.rsplit("/", 1)[-1])
    SwitchController(0, user)
    output = b''
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def login():
    controller = LoginController()
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status

def api_auth(params):
    try:
        controller = AuthController(params)
        uid = controller.response().encode('utf-8')
        output = b''
        status = '302 Found'
        response_headers = [('Content-type', 'text/html'),
                            ('Content-Length', str(len(output))),
                            ('Location', f'https://iot.yujiezhu.net/web/dashboard/{uid}')]
        return output, response_headers, status
    except:
        return login()

def application(environ, start_response):
    path = environ['PATH_INFO']
    params = {}

    if 'QUERY_STRING' in environ and str(environ['QUERY_STRING']) != "":
        query_list = str(environ['QUERY_STRING']).split("&")
        for item in query_list:
            param = item.split("=")
            params.update({param[0]: param[1]})

    if path == '/api/auth' in path:
        output, response_headers, status = api_auth(params)
        start_response(status, response_headers)
        return [output]

    if path == '/web/login' or path == '/':
        output, response_headers, status = login()
        start_response(status, response_headers)
        return [output]

    if '/api/on' in path:
        output, response_headers, status = api_on(path)
        start_response(status, response_headers)
        return [output]

    if '/api/off' in path:
        output, response_headers, status = api_off(path)
        start_response(status, response_headers)
        return [output]

    if '/web/dashboard' in path:
        output, response_headers, status = web_dashboard(path)
        start_response(status, response_headers)
        return [output]

    if path == '/api/water-level':
        output, response_headers, status = api_water_level(params)
        start_response(status, response_headers)
        return [output]

    if path == '/api/status':
        output, response_headers, status = api_status(params)
        start_response(status, response_headers)
        return [output]


    status = '404 Not Found'
    output = b'404 Page Not Found'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]


if __name__ == '__main__':
    environ1 = {'PATH_INFO': '/api/water-level',
               'REQUEST_METHOD': 'GET',
               'QUERY_STRING': 'level=80&user=1'}
    environ2 = {'PATH_INFO': '/api/status',
               'REQUEST_METHOD': 'GET',
               'QUERY_STRING': 'user=1'}
    environ3 = {'PATH_INFO': '/web/dashboard/1',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': 'user=1'}
    environ4 = {'PATH_INFO': '/web/login',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': ''}
    environ5 = {'PATH_INFO': '/web/register',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': ''}
    environ6 = {'PATH_INFO': '/',
                'REQUEST_METHOD': 'GET',
                'QUERY_STRING': ''}
    output = application(environ6, start_response)
    print(output[0])
    # print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    # Connection().initialize()
