import sqlite3

class databaseConnection():
    def connect(self):
        try:
            conn = sqlite3.connect('example.db')
            print("Connection to database is successful")
            return conn
        except :
            print("Connection to database is not successful")

    def getCursor(self, conn):
        cursor = conn.cursor()
        return cursor
    
    def executeSql(self, cursor, sql):
          
        try:
            cursor.execute(sql)
            print("Sql executed")
        except:
            print("Sql no executed")
     
     