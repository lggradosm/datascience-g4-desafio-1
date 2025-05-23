import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "password"
        self.port = 3306
        self.database = "db_g4"
    
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host= self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            return connection
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def execute_query(self, query):
        connection = None
        cursor = None   
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()


