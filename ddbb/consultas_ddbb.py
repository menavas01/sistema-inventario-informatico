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

def cargar_equipo_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_tipo, tipo FROM tipo_de_equipo")
    
    tipos_de_equipo = {row[0]: row[1] for row in cursor.fetchall()}
    id_tipo = next(key for key, value in tipos_de_equipo.items() if value == datos[3])
    
    cursor.execute("INSERT INTO equipo (marca, modelo, serie, tipo_id) VALUES (?, ?, ?, ?)", (datos[0], datos[1], datos[2], id_tipo))
    conn.commit()
    conn.close()
    
def cargar_asignacion_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    
    serie = datos[0].split("|")[1].strip()
    cursor.execute("SELECT id_equipo FROM equipo WHERE serie = ?", [serie])
    id_equipo = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO asignacion (equipo_id, usuario, motivo_asignacion, fecha_asignacion) VALUES (?, ?, ?, ?)", (id_equipo, datos[1], datos[2], datos[3]))
    cursor.execute("DELETE FROM equipo WHERE id_equipo = ?", [id_equipo])
    conn.commit()
    conn.close()
    
def cargar_baja_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    
    serie = datos[0].split("|")[1].strip()
    cursor.execute("SELECT id_equipo FROM equipo WHERE serie = ?", [serie])
    id_equipo = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO bajas (equipo_id, motivo_baja, fecha_baja, detalles_equipo) VALUES (?, ?, ?, ?)", (id_equipo, datos[1], datos[2], datos[0]))
    cursor.execute("DELETE FROM equipo WHERE id_equipo = ?", [id_equipo])
    
    
    cursor.execute("SELECT id_asignacion FROM asignacion WHERE equipo_id = ?", [id_equipo])
    asignacion = cursor.fetchall()
    
    if (asignacion != []):
        cursor.execute("DELETE FROM asignacion WHERE equipo_id = ?", [id_equipo])
    
    
    conn.commit()
    conn.close()

def obtener_todos_los_equipos():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT equipo.id_equipo, tipo_de_equipo.tipo, equipo.marca, equipo.modelo, equipo.serie
    FROM equipo
    JOIN tipo_de_equipo ON equipo.tipo_id = tipo_de_equipo.id_tipo
    ''')
    equipos = cursor.fetchall()
    conn.close()
    return equipos

def obtener_todas_las_bajas():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT equipo_id, motivo_baja, fecha_baja, detalles_equipo
    FROM bajas
    ''')
    bajas = cursor.fetchall()
    conn.close()
    return bajas

def obtener_todas_las_asignaciones():
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT equipo_id, usuario, motivo_asignacion, fecha_asignacion
    FROM asignacion
    ''')
    bajas = cursor.fetchall()
    conn.close()
    return bajas

def eliminar_equipo(id_equipo):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM equipo WHERE id_equipo = ?", [id_equipo])
    conn.commit()
    conn.close()
    
def eliminar_asignacion(id_asignacion):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM asignacion WHERE equipo_id = ?", [id_asignacion])
    conn.commit()
    conn.close()
    
def eliminar_baja(id_baja):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bajas WHERE equipo_id = ?", [id_baja])
    conn.commit()
    conn.close()

def editar_equipo_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_tipo, tipo FROM tipo_de_equipo")
    
    tipos_de_equipo = {row[0]: row[1] for row in cursor.fetchall()}
    id_tipo = next(key for key, value in tipos_de_equipo.items() if value == datos[4])
    
    cursor.execute("UPDATE equipo SET marca = ?, modelo = ?, serie = ?, tipo_id = ? WHERE id_equipo = ?", (datos[1], datos[2], datos[3],id_tipo,datos[0]))
    
    conn.commit()
    conn.close()
    
def editar_bajas_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE bajas SET motivo_baja = ?, fecha_baja = ? WHERE equipo_id = ?", (datos[1], datos[2], datos[0]))
    
    conn.commit()
    conn.close()
    
def editar_asignacion_ddbb(datos):
    conn = sqlite3.connect('ddbb/equipos.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE asignacion SET usuario = ?, motivo_asignacion = ?, fecha_asignacion = ? WHERE equipo_id = ?", (datos[1], datos[2], datos[3], datos[0]))
    
    conn.commit()
    conn.close()


