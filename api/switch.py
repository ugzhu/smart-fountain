from db.connection import Connection


class SwitchController():
    def __init__(self, status, user_id):
        self.status = status
        self.id = user_id
        self.switch()

    def switch(self):
        sql = f"UPDATE Status SET status = {self.status} WHERE UID = {self.id}"
        conn = Connection()
        conn.execute(sql)
