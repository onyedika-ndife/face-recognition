import mysql.connector as sql
from mysql.connector import errorcode


class Database:
    def __init__(self):
        try:
            self.conn = sql.connect(
                host="localhost",
                user="root",
                password="C!$c@123",
                database="FaceBase",
                autocommit=False,
            )
            if self.conn.is_connected():
                print("Database Connected")
        except sql.Error as err:
            if errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(errorcode)
        else:
            # Database Cursor
            self.cur = self.conn.cursor()
