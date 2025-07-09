import sqlite3

class Conexion():
    def conexion(self):
        self.conn = sqlite3.connect("equipos.db")
        self.cursor = self.conn.cursor()
        
    def cerrar_db(self):
        self.conn.commit()
        self.conn.close()
