from db.connection import Connection
import os


class DashboardController():
    def __init__(self, params):
        self.userId = params['user']

    def response(self):
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/dashboard.html"
        with open(path) as f:
            for line in f:
                response = response + str(line)
        return response
