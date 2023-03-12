from db.connection import Connection

class NewUserController:
    def __init__(self, params):
        self.username = params['username']
        self.password = params['password']

    def response(self):
        sql = f"INSERT INTO Usr(username, password, activation)" \
              f"VALUES('{self.username}', '{self.password}', 0);"
        conn = Connection()
        conn.execute(sql)
