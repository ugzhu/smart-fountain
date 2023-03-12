from db.connection import Connection
import os


class DashboardController():
    def __init__(self, user):
        self.userId = user

    def response(self):
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/dashboard.html"
        parameters = f"""
                    var xValues1 = [50,60,70,80,90,100,110,120,130,140,150];/n
                    var yValues1 = [7,8,8,9,9,9,10,11,14,14,15];/n
                    var xValues2 = [50,60,70,80,90,100,110,120,130,140,150];/n
                    var yValues2 = [7,8,8,9,9,9,10,11,14,14,15];/n
                    """
        with open(path) as f:
            for line in f:
                if "{% customer insert indicator %}" in line:
                    response = response + parameters
                    continue
                response = response + line

        return response
