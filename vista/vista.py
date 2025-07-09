from tkinter import ttk, StringVar, OptionMenu
from ddbb.consultas_ddbb import obtener_tipos_equipo

class CargarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana

        self.label = ttk.Label (self.ventana, text = "Cargar equipo", font = ("system-ui",11))
        
        self.marca = ttk.Entry(self.ventana)
        self.modelo = ttk.Entry(self.ventana)
        self.serie = ttk.Entry(self.ventana)
        
        equipos = obtener_tipos_equipo()
        self.tipoEquipo = ttk.Combobox(state = "readonly", values = equipos)
        self.tipoEquipo.set("Selecciona una opcion")

        self.cargar = ttk.Button(self.ventana, text = "Cargar", command = self.cargar_equipos)

    def cargar_equipos(self):
        print ("Equipo cargado")

    def mostrar(self):
        self.label.pack()
        self.marca.pack()
        self.modelo.pack()
        self.serie.pack()
        self.tipoEquipo.pack()
        self.cargar.pack()
        
