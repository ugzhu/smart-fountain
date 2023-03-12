from db.connection import Connection


class SwitchController():
    def __init__(self, switch, user_id):
        self.switch = switch
        self.id = user_id
        switch()

    def switch(self):
        sql = f"UPDATE Status SET status = {self.switch()} WHERE UID = {self.id}"
        conn = Connection()
        conn.execute(sql)
