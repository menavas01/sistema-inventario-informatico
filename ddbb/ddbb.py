import sqlite3

class Conexion():
    def conexion(self):
        self.conn = sqlite3.connect("equipos.db")
        self.cursor = self.conn.cursor()
        
    def cerrar_db(self):
        self.conn.commit()
        self.conn.close()
        
def listar_equipos():
    equipos = Conexion()
    listar_equipos = []

    sql= f'''
        SELECT e.id_equipo,e.serie,e.marca,e.modelo, t.tipo FROM equipo as e
        INNER JOIN tipo_de_equipo as t
        ON e.tipo_id = t.id_tipo;
'''
    try:
        equipos.cursor.execute(sql)
        listar_equipos = equipos.cursor.fetchall()
        equipos.cerrar_db()
        print(listar_equipos)
        return listar_equipos
    except:
        pass
