import mysql.connector

class Conexion:
    def __init__(self):
        self.config = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "invernaderos"
        }

    def conectar(self):
        try:
            conn = mysql.connector.connect(**self.config)
            if conn.is_connected():
                return conn
        except mysql.connector.Error as e:
            print("Error de conexión:", e)
            return None
