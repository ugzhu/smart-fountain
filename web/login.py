from db.connection import Connection
import os


class LoginController:
    def __init__(self):
        pass

    @staticmethod
    def response():
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/login.html"

        with open(path) as f:
            for line in f:
                response += line

        return response
