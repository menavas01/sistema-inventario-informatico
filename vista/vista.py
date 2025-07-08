from tkinter import ttk, StringVar, OptionMenu

class CargarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana

        self.label = ttk.Label (self.ventana, text = "Cargar equipo", font = ("system-ui",11))
        self.marca = ttk.Entry(self.ventana)
        self.modelo = ttk.Entry(self.ventana)
        self.serie = ttk.Entry(self.ventana)

        valor_inicial = StringVar(value="Selecciona una opcion")
        opciones = ["Opcion 1", "Opcion 2"]
        self.tipoEquipo = ttk.OptionMenu(self.ventana, valor_inicial, *opciones)

        self.cargar = ttk.Button(self.ventana, text="Cargar", command=self.cargar_equipos)

    def cargar_equipos():
        #Hacer inputs como una lista para cargarlo
        equipo = []

    def mostrar(self):
        self.label.pack()
        self.marca.pack()
        self.modelo.pack()
        self.serie.pack()
        self.tipoEquipo.pack()
        self.cargar.pack()
        
