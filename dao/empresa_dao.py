from config.database import Database
from model.empresa import Empresa
class EmpresaDAO:
    def __init__ (self):
        self.database = Database()

    def get_all(self):
        cursor = None
        connection = None
        try:
            query = """
                SELECT * FROM empresa WHERE estado = 1
            """ 
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
    
    def insert(self, empresa):
        connection = None
        cursor = None
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()

            select_query = "SELECT id FROM empresa WHERE ruc = %s AND estado = 0"
            cursor.execute(select_query, (empresa.ruc,))
            result = cursor.fetchone()

            if result:
                update_query = "UPDATE empresa SET estado = 1 WHERE id = %s"
                cursor.execute(update_query, (result[0],))
            else:
                insert_query = """
                    INSERT INTO empresa (ruc, razon_social, direccion, estado)
                    VALUES (%s, %s, %s, 1)
                """
                cursor.execute(insert_query, (empresa.ruc, empresa.razon_social, empresa.direccion))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    def delete(self, empresa_id):
        connection = None
        cursor = None
        try:
            query = """
                UPDATE empresa SET estado = 0 WHERE id = %s
            """
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (empresa_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally: 
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
        
        