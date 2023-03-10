import concurrent.futures
import sqlite3
import os

class Connection:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "/db.sqlite3"
        print(path)
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def execute(self, sql):
        response = self.cur.execute(sql)
        self.con.commit()
        return response

    def initialize(self):
        sql = ["""
                CREATE TABLE Usr(
                UID INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
                );
                """,
               """
                CREATE TABLE Level(
                LID INTEGER PRIMARY KEY AUTOINCREMENT,
                level VARCHAR(255) NOT NULL,
                time VARCHAR(255) NOT NULL,
                UID INTEGER,
                FOREIGN KEY (UID) REFERENCES Usr(UID) ON DELETE CASCADE
                );
                """,
               """
                CREATE TABLE Status(
                SID INTEGER PRIMARY KEY AUTOINCREMENT,
                status VARCHAR(255) NOT NULL,
                UID INTEGER,
                FOREIGN KEY (UID) REFERENCES Usr(UID) ON DELETE CASCADE
                );
                """,
               """
                INSERT INTO Status(status, UID)
                VALUES ('1', '1');
                """,
               """
               INSERT INTO Usr(username, password)
               VALUES ('test', 'test');
               """
               ]
        for s in sql:
            response = self.cur.execute(s)
            print(response)
            self.con.commit()
