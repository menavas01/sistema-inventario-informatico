from tkinter import ttk
from ddbb.consultas_ddbb import obtener_tipos_equipo

class CargarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Cargar equipo", font = ("system-ui",11))
        
        self.marca = ttk.Entry(self.frame)
        self.modelo = ttk.Entry(self.frame)
        self.serie = ttk.Entry(self.frame)
        
        equipos = obtener_tipos_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = equipos)
        self.tipoEquipo.set("Selecciona una opcion")

        self.cargar = ttk.Button(self.frame, text = "Cargar", command = self.cargar_equipos)

    def cargar_equipos(self):
        print ("Equipo cargado")

    def mostrar_carga(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.marca.pack(padx= 10, pady= 10)
        self.modelo.pack(padx= 10, pady= 10)
        self.serie.pack(padx= 10, pady= 10)
        self.tipoEquipo.pack(padx= 10, pady= 10)
        self.cargar.pack(padx= 10, pady= 10)
        
    def ocultar(self):
        self.frame.pack_forget()