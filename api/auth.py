from db.connection import Connection

class AuthController:
    def __init__(self, params):
        self.username = params['username']
        self.password = params['password']

    def response(self):
        sql = f"SELECT UID FROM Usr WHERE username = '{self.username}' AND password = '{self.password}';"
        print(sql)
        conn = Connection()
        return conn.execute(sql).fetchone()[0]