import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas_ddbb import obtener_equipo, cargar_asignacion_ddbb, obtener_todos_los_equipos
from tkcalendar import DateEntry
from datetime import datetime

class AsignacionEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Asignar equipo", font = ("system-ui",11))
        
        self.tipoEquipo_label = ttk.Label(self.frame, text="Seleccione un equipo")
        equipos = obtener_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = equipos, width = 47)
        self.tipoEquipo.set("Selecciona una opcion")
        
        self.usuario_label = ttk.Label(self.frame, text="Usuario asignado")
        self.usuario = ttk.Entry(self.frame, width = 50)
        self.motivo_label = ttk.Label(self.frame, text="Motivo de asignacion")
        self.motivo = ttk.Entry(self.frame, width = 50)
        self.fecha_label = ttk.Label(self.frame, text="Fecha de asignacion")
        self.fecha = DateEntry(self.frame, date_pattern = "dd/mm/yyyy", width = 47)

        self.asignar = ttk.Button(self.frame, text = "Asignar", command = self.asignacion_equipos, width = 50)

    def asignacion_equipos(self):
        if self.tipoEquipo.get() == "Selecciona una opcion":
            messagebox.showerror("Error", "Por favor, selecciona una opción válida")
            return
        if not all([self.usuario.get(), self.motivo.get()]):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return
        
        datos_equipo = [
            self.tipoEquipo.get(),
            self.usuario.get(),
            self.motivo.get(),
            self.fecha.get(),
        ]
        
        try:
            cargar_asignacion_ddbb(datos_equipo)
            messagebox.showinfo("Éxito", f"Equipo asignado: {', '.join(datos_equipo)}")
            self.motivo.delete(0, tk.END)
            self.usuario.delete(0, tk.END)
            self.fecha.set_date(datetime.now())
            self.tipoEquipo.set("Selecciona una opción")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el equipo: {e}")

    def eliminar_equipo(self, id_equipo):
        import sqlite3
        conn = sqlite3.connect('ddbb/equipos.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM equipo WHERE id_equipo = ?', (id_equipo,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Revertido', 'Equipo eliminado correctamente')
        self.frame.pack_forget()
        self.mostrar_asignacion()

    def mostrar_lista_equipos(self):
        contenedor = ttk.Frame(self.frame)
        contenedor.pack(padx=10, pady=10, fill='both', expand=True)
        canvas = tk.Canvas(contenedor, height=150)
        scrollbar = ttk.Scrollbar(contenedor, orient='vertical', command=canvas.yview)
        frame_lista = ttk.Frame(canvas)
        frame_lista.bind(
            '<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
        )
        canvas.create_window((0, 0), window=frame_lista, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        equipos = obtener_todos_los_equipos()
        for eq in equipos:
            info = f"{eq[1]} | Marca: {eq[2]} | Modelo: {eq[3]} | Serie: {eq[4]}"
            fila = ttk.Frame(frame_lista)
            fila.pack(fill='x', padx=5, pady=2)
            ttk.Label(fila, text=info, anchor='w').pack(side='left', fill='x', expand=True)
            ttk.Button(fila, text='Revertir', command=lambda i=eq[0]: self.eliminar_equipo(i)).pack(side='right')

    def mostrar_asignacion(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.tipoEquipo_label.pack(anchor="w")
        self.tipoEquipo.pack(padx= 10, pady= (10, 20))
        self.usuario_label.pack(anchor="w")
        self.usuario.pack(padx= 10, pady= (10, 20))
        self.motivo_label.pack(anchor="w")
        self.motivo.pack(padx= 10, pady= (10, 20))
        self.fecha_label.pack(anchor="w")
        self.fecha.pack(padx= 10, pady= 10)
        self.asignar.pack(padx= 10, pady= 10)
        self.mostrar_lista_equipos()
        
    def ocultar(self):
        self.frame.pack_forget()