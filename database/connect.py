from database.database import databaseConnection

def load_db():
    conn = databaseConnection()
    conn.connect()
    conn.getCursor()
    return conn

def close_db(conn):
    conn.commit()    
    conn.close()
    return 1