import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas_ddbb import obtener_equipo, cargar_asignacion_ddbb, obtener_todas_las_asignaciones, eliminar_asignacion, editar_asignacion_ddbb
from tkcalendar import DateEntry
from datetime import datetime

class AsignacionEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Asignar equipo", font = ("system-ui",11))
        
        self.tipoEquipo_label = ttk.Label(self.frame, text="Seleccione un equipo")
        self.equipos = obtener_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = self.equipos, width = 47)
        self.tipoEquipo.set("Selecciona una opcion")
        
        self.usuario_label = ttk.Label(self.frame, text="Usuario asignado")
        self.usuario = ttk.Entry(self.frame, width = 50)
        self.motivo_label = ttk.Label(self.frame, text="Motivo de asignacion")
        self.motivo = ttk.Entry(self.frame, width = 50)
        self.fecha_label = ttk.Label(self.frame, text="Fecha de asignacion")
        self.fecha = DateEntry(self.frame, date_pattern = "dd/mm/yyyy", width = 47)

        self.lista_a = obtener_todas_las_asignaciones()
        self.lista_a.reverse()
        self.frame_tabla = ttk.Frame(self.ventana)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("Motivo","Fecha","Detalles"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky="nse")

        self.tabla.heading("#0", text="ID del equipo")
        self.tabla.heading("#1", text="Usuario")
        self.tabla.heading("#2", text="Motivo")
        self.tabla.heading("#3", text="Fecha")
        for a in self.lista_a:
            self.tabla.insert('',0,text=a[0],
                              values=(a[1],a[2],a[3]))
            
        self.menu = tk.Menu(self.ventana, tearoff=0)
        self.menu.add_command(label="Editar", command=self.editar)
        self.menu.add_command(label="Eliminar", command=self.eliminar)
        self.tabla.bind("<Button-3>", self.on_right_click)

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
        self.mostrar_asignacion()

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
        self.frame_tabla.pack()
        self.tabla.pack(padx= 10, pady= 20)
        self.asignar.pack(padx= 10, pady= 10)
        
    def ocultar(self):
        self.frame.pack_forget()
        self.frame_tabla.pack_forget()
        
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        self.lista_a = obtener_todas_las_asignaciones()
        self.lista_a.reverse()

        for a in self.lista_a:
            self.tabla.insert('',0,text=a[0],
                              values=(a[1],a[2],a[3]))
            
    def on_right_click(self, event):
        self.item_id = self.tabla.identify_row(event.y)
        self.id_equipo = self.tabla.item(self.item_id, "text")
        if self.item_id:
            self.tabla.selection_set(self.item_id)
            self.menu.post(event.x_root, event.y_root)
    
    def eliminar(self):
        eliminar_asignacion(self.id_equipo)
        self.actualizar_tabla()
        
    def editar(self):
        self.edicion = tk.Toplevel(self.ventana)
        
        self.edicion.title("Sistema de Inventario")  
        self.edicion.iconbitmap("assets/icon.ico")
        self.edicion.geometry("400x500")
        
        frame_edicion = ttk.Frame(self.edicion)
        frame_edicion.pack(padx=10, pady=10, fill="both", expand=True)

        label = ttk.Label(frame_edicion, text="Editar asignacion", font=("system-ui", 11))
        label.pack(pady=10)

        usuario_label = ttk.Label(frame_edicion, text="Usuario asignado")
        usuario_label.pack(anchor="w")
        usuario_entry = ttk.Entry(frame_edicion, width=50)
        usuario_entry.insert(0, self.tabla.item(self.item_id)["values"][0])
        usuario_entry.pack(pady=(0, 10))

        motivo_label = ttk.Label(frame_edicion, text="Motivo de asignacion")
        motivo_label.pack(anchor="w")
        motivo_entry = ttk.Entry(frame_edicion, width=50)
        motivo_entry.insert(0, self.tabla.item(self.item_id)["values"][1])
        motivo_entry.pack(pady=(0, 10))

        fecha_label = ttk.Label(frame_edicion, text="Fecha de asignacion")
        fecha_label.pack(anchor="w")
        fecha_dateentry = DateEntry(frame_edicion, date_pattern = "dd/mm/yyyy", width = 47)
        fecha_asignacion = datetime.strptime(self.tabla.item(self.item_id)["values"][2], "%d/%m/%Y").date()
        fecha_dateentry.set_date(fecha_asignacion)
        fecha_dateentry.pack(pady=(0, 10))
        
        def confirmar_edicion():
            id_equipo = str(self.tabla.item(self.item_id, "text"))
            datos_equipo = [
                id_equipo,
                usuario_entry.get(),
                motivo_entry.get(),
                fecha_dateentry.get()
            ] 
            
            try:
                editar_asignacion_ddbb(datos_equipo)
                messagebox.showinfo("Éxito", f"Equipo editado: {', '.join(datos_equipo)}")
                self.edicion.destroy()
                self.actualizar_tabla()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo editar el equipo: {e}")
        guardar = ttk.Button(frame_edicion, text = "Guardar", command = confirmar_edicion, width = 50)
        guardar.pack(padx= 10, pady= 10)
        