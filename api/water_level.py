from datetime import datetime
from db.connection import Connection


class WaterLevelController:
    def __init__(self, params):
        self.userId = 1
        self.time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.level = params['level']

    def response(self):
        sql = f"""
        INSERT INTO Level(level, time, UID)
        VALUES ('{self.level}', '{self.time}', 1);
        """
        conn = Connection()
        conn.execute(sql)
        return ''
