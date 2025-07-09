from tkinter import ttk
from ddbb.consultas_ddbb import obtener_tipos_equipo

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

        self.cargar = ttk.Button(self.frame, text = "Cargar", command = self.cargar_equipos, width = 50)

    def cargar_equipos(self):
        print ("Equipo cargado")

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
        
    def ocultar(self):
        self.frame.pack_forget()