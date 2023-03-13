from datetime import datetime
from db.connection import Connection
import pytz

class WaterLevelController:
    def __init__(self, params):
        self.userId = params['user']
        self.time = datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime("%Y/%m/%d %H:%M:%S")
        self.level = params['level']
        print(self.time)
        print(type(self.time))

    def response(self):
        sql = f"""
        INSERT INTO Level(level, time, UID)
        VALUES ('{self.level}', '{self.time}', 1);
        """
        conn = Connection()
        conn.execute(sql)
        return ''
