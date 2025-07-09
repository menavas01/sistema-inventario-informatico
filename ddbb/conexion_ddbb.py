import sqlite3

class Conexion():
    def conexion(self):
        self.conn = sqlite3.connect('ddbb/equipos.db')
        self.cursor = self.conn.cursor()
        return self.cursor
        
    def desconectar(self):
        self.conn.close()