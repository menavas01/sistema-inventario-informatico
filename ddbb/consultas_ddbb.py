import sqlite3

def obtener_tipos_equipo():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM tipo_de_equipo")
    tipos = []
    for row in cursor.fetchall():
        tipos.append(row[0])
    conn.close()
    return tipos

def obtener_equipo():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT tipo_de_equipo.tipo || ' - ' || marca || ' ' || modelo || ' | ' || serie AS equipo_completo 
    FROM equipo 
    JOIN tipo_de_equipo ON equipo.tipo_id = tipo_de_equipo.id_tipo
    """)
    equipos = []
    for row in cursor.fetchall():
        equipos.append(row[0])
    conn.close()
    return equipos