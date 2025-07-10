import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas_ddbb import obtener_equipo, cargar_asignacion_ddbb
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
        
    def ocultar(self):
        self.frame.pack_forget()