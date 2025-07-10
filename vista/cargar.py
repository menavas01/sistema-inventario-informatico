import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas_ddbb import obtener_tipos_equipo, cargar_equipo_ddbb, obtener_todos_los_equipos

class CargarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Cargar equipo", font = ("system-ui",11))
        
        self.marca_label = ttk.Label (self.frame, text = "Ingrese marca del equipo")
        self.marca = ttk.Entry(self.frame, width = 50)
        
        self.modelo_label = ttk.Label (self.frame, text = "Ingrese modelo del equipo")
        self.modelo = ttk.Entry(self.frame, width = 50)
        
        self.serie_label = ttk.Label (self.frame, text = "Ingrese serie del equipo")
        self.serie = ttk.Entry(self.frame, width = 50)
        
        self.tipoEquipo_label = ttk.Label (self.frame, text = "Seleccione el tipo de equipo")
        equipos = obtener_tipos_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = equipos, width = 47)
        self.tipoEquipo.set("Selecciona una opcion")

        self.lista_e = obtener_todos_los_equipos()
        self.lista_e.reverse()
        self.frame_tabla = ttk.Frame(self.ventana)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("Serie","Marca","Modelo", "Tipo"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky="nse")

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Tipo")
        self.tabla.heading("#2", text="Marca")
        self.tabla.heading("#3", text="Modelo")
        self.tabla.heading("#4", text="Serie")

        for e in self.lista_e:
            self.tabla.insert('',0,text=e[0],
                              values=(e[1],e[2],e[3],e[4]))

        self.cargar = ttk.Button(self.frame, text = "Cargar", command = self.cargar_equipos, width = 50)

    def cargar_equipos(self):
        if self.tipoEquipo.get() == "Selecciona una opcion":
            messagebox.showerror("Error", "Por favor, selecciona una opción válida")
            return
        if not all([self.marca.get(), self.modelo.get(), self.serie.get()]):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return
        
        datos_equipo = [
            self.marca.get(),
            self.modelo.get(),
            self.serie.get(),
            self.tipoEquipo.get()
        ]
        
        try:
            cargar_equipo_ddbb(datos_equipo)
            messagebox.showinfo("Éxito", f"Equipo cargado: {', '.join(datos_equipo)}")
            self.marca.delete(0, tk.END)
            self.modelo.delete(0, tk.END)
            self.serie.delete(0, tk.END)
            self.tipoEquipo.set("Selecciona una opción")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el equipo: {e}")

    def mostrar_carga(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.marca_label.pack(anchor="w")
        self.marca.pack(padx= 10, pady= (10, 20))
        self.modelo_label.pack(anchor="w")
        self.modelo.pack(padx= 10, pady= (10, 20))
        self.serie_label.pack(anchor="w")
        self.serie.pack(padx= 10, pady= 10)
        self.tipoEquipo_label.pack(anchor="w")
        self.tipoEquipo.pack(padx= 10, pady= 10)
        self.cargar.pack(padx= 10, pady= 10)
        self.frame_tabla.pack()
        self.tabla.pack(padx= 10, pady= 20)
        
    def ocultar(self):
        self.frame.pack_forget()
        self.frame_tabla.pack_forget()