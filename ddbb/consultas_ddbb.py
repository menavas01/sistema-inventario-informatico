import sqlite3
from ddbb.conectar_ddbb import Conexion
    
def obtener_tipos_equipo():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM tipo_de_equipo")
    tipos = []
    for row in cursor.fetchall():
        tipos.append(row[0])
    conn.close()
    return tipos