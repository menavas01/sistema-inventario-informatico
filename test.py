import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Obtener los tipos de equipo desde la base de datos
def obtener_tipos_equipo():
    conn = sqlite3.connect('ddbb/equipos.db')  # Asegúrate de que 'equipos.db' sea el nombre correcto
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM tipo_de_equipo")
    tipos = []
    for row in cursor.fetchall():
        tipos.append(row[0])
    conn.close()
    return tipos

# Función para manejar la selección del Combobox
def seleccionar_equipo(event):
    seleccion = combo_equipo.get()
    messagebox.showinfo("Selección", f"Has seleccionado: {seleccion}")

# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Tipo de Equipo")
root.geometry("300x150")

# Crear etiqueta
label = tk.Label(root, text="Selecciona un tipo de equipo:")
label.pack(pady=10)

# Crear Combobox con los tipos de equipo
tipos = obtener_tipos_equipo()
combo_equipo = ttk.Combobox(root, values=tipos, state="readonly")
combo_equipo.pack(pady=10)
combo_equipo.bind("<<ComboboxSelected>>", seleccionar_equipo)

# Botón para cerrar la ventana
boton_cerrar = tk.Button(root, text="Cerrar", command=root.quit)
boton_cerrar.pack(pady=10)

# Iniciar la aplicación
root.mainloop()