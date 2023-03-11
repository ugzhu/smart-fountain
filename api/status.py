from db.connection import Connection


class StatusController:
    def __init__(self, params):
        self.userId = params['user']

    def response(self):
        sql = f"SELECT status FROM Status WHERE UID = {self.userId}"
        conn = Connection()
        response = str(conn.execute(sql).fetchone()[0])
        return response
