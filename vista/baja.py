import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas_ddbb import obtener_equipo, cargar_baja_ddbb, obtener_todas_las_bajas
from tkcalendar import DateEntry
from datetime import datetime

class BajaEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Baja equipo", font = ("system-ui",11))
        
        self.tipoEquipo_label = ttk.Label (self.frame, text = "Seleccione un equipo")
        self.equipos = obtener_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = self.equipos, width = 47)
        self.tipoEquipo.set("Selecciona una opcion")
        
        self.motivo_label = ttk.Label (self.frame, text = "Motivo de baja")
        self.motivo = ttk.Entry(self.frame, width = 50)
        
        self.fecha_label = ttk.Label (self.frame, text = "Fecha de baja")
        self.fecha = DateEntry(self.frame, date_pattern = "dd/mm/yyyy", width = 47)

        self.lista_b = obtener_todas_las_bajas()
        self.lista_b.reverse()
        self.frame_tabla = ttk.Frame(self.ventana)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("Motivo","Fecha","Detalles"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky="nse")

        self.tabla.heading("#0", text="ID del equipo")
        self.tabla.heading("#1", text="Motivo")
        self.tabla.heading("#2", text="Fecha")
        self.tabla.heading("#3", text="Detalles")
        for b in self.lista_b:
            self.tabla.insert('',0,text=b[0],
                              values=(b[1],b[2],b[3]))
            
        self.menu = tk.Menu(self.ventana, tearoff=0)
        self.menu.add_command(label="Editar", command=self.editar)
        self.menu.add_command(label="Eliminar", command=self.eliminar)
        self.tabla.bind("<Button-3>", self.on_right_click)

        self.baja = ttk.Button(self.frame, text = "Dar de baja", command = self.baja_equipos, width = 50)

    def baja_equipos(self):
        if self.tipoEquipo.get() == "Selecciona una opcion":
            messagebox.showerror("Error", "Por favor, selecciona una opción válida")
            return
        if not all([self.motivo.get(), self.fecha.get()]):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return
        
        datos_equipo = [
            self.tipoEquipo.get(),
            self.motivo.get(),
            self.fecha.get(),
        ]
        
        try:
            cargar_baja_ddbb(datos_equipo)
            messagebox.showinfo("Éxito", f"Equipo dado de baja: {', '.join(datos_equipo)}")
            self.motivo.delete(0, tk.END)
            self.fecha.set_date(datetime.now())
            self.tipoEquipo.set("Selecciona una opción")
            self.equipos = obtener_equipo()
            self.actualizar_tabla()
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
        self.mostrar_baja()

    def mostrar_baja(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.tipoEquipo_label.pack(anchor="w")
        self.tipoEquipo.pack(padx= 10, pady= (10, 20))
        self.motivo_label.pack(anchor="w")
        self.motivo.pack(padx= 10, pady= (10, 20))
        self.fecha_label.pack(anchor="w")
        self.fecha.pack(padx= 10, pady= 10)
        self.frame_tabla.pack()
        self.tabla.pack(padx= 10, pady= 20)
        self.baja.pack(padx= 10, pady= 10)
        
    def ocultar(self):
        self.frame.pack_forget()
        self.frame_tabla.pack_forget()
        
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        self.lista_b = obtener_todas_las_bajas()
        self.lista_b.reverse()

        for b in self.lista_b:
            self.tabla.insert('',0,text=b[0],
                              values=(b[1],b[2],b[3]))
            
    def on_right_click(self, event):
        self.item_id = self.tabla.identify_row(event.y)
        self.id_equipo = self.tabla.item(self.item_id, "text")
        if self.item_id:
            self.tabla.selection_set(self.item_id)
            self.menu.post(event.x_root, event.y_root)
            
    def editar(self):
        pass
    
    def eliminar(self):
        pass