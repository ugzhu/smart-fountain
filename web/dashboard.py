from db.connection import Connection
from datetime import datetime
import pytz
import os


class DashboardController():
    def __init__(self, user):
        self.userId = user
        self.conn = Connection()
        self.username = self.get_user_name()
        self.activation = self.get_activation()
        if self.activation != 1:
            return
        self.x1, self.y1, self.x2, self.y2 = self.get_params()
        self.status = self.get_status()


    def get_activation(self):
        try:
            sql = f"SELECT activation FROM Usr WHERE UID = {self.userId};"
            activation = int(self.conn.execute(sql).fetchone()[0])
        except:
            activation = 0
        return activation

    def get_status(self):
        sql = f"SELECT status FROM Status WHERE UID = {self.userId};"
        status = int(self.conn.execute(sql).fetchone()[0])
        if status == 1:
            return '<em class="switch-on" id="status">ON</em>'
        return '<em class="switch-off" id="status">OFF</em>'

    def get_user_name(self):
        sql = f"SELECT username FROM Usr WHERE UID = {self.userId};"
        username = self.conn.execute(sql).fetchone()[0]
        print(username)
        return username

    def get_params(self):
        today = datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime("%Y/%m/%d")
        sql = f"SELECT time, level FROM Level WHERE UID = {self.userId};"
        levels = self.conn.execute(sql).fetchall()
        history_params = self.sort(levels)
        today_params = []
        for item in history_params:
            if today in item[0]:
                today_params.append(item)
        x_values1, y_values1 = self.params_to_string(today_params)
        x_values2, y_values2 = self.params_to_string(history_params)
        return x_values1, y_values1, x_values2, y_values2

    @staticmethod
    def params_to_string(params):
        xValues, yValues = "[", "["
        for param in params:
            xValues += f"'{param[0]}', "
            yValues += f"{param[1]}, "
        xValues += "]"
        yValues += "]"
        return xValues, yValues

    @staticmethod
    def sort(my_list):
        new_list = []
        res_list = []

        for item in my_list:
            new_list.append((datetime.strptime(item[0], "%Y/%m/%d %H:%M:%S"), item[1]))

        new_list = sorted(new_list)

        for item in new_list:
            res_list.append((item[0].strftime("%Y/%m/%d %H:%M:%S"), item[1]))

        return res_list

    def not_active(self):
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/not-active.html"
        with open(path) as f:
            for line in f:
                if "{% user %}" in line:
                    response += line.replace("{% user %}", self.username)
                    continue
                response += line

        return response


    def response(self):
        if self.activation != 1:
            return self.not_active()
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/dashboard.html"
        insert = f"""\
var userId = '{self.userId}';
var xValues1 = {self.x1};
var yValues1 = {self.y1};
var xValues2 = {self.x2};
var yValues2 = {self.y2};
"""
        with open(path) as f:
            for line in f:
                if "{% status %}" in line:
                    response += self.status
                    continue
                if "{% user %}" in line:
                    response += line.replace("{% user %}", self.username)
                    continue
                if "{% customized insert indicator %}" in line:
                    response += insert
                    continue
                response += line

        return response
