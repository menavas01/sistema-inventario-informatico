from tkinter import ttk

class CargarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana

        self.label = ttk.Label (self.ventana, text = "Cargar equipo", font = ("system-ui",11))
        self.marca = ttk.Entry(self.ventana)
        self.modelo = ttk.Entry(self.ventana)
        self.serie = ttk.Entry(self.ventana)
        self.tipoEquipo = ttk.Entry(self.ventana)

        self.cargar = ttk.Button(self.root, text="Cargar", command=self.cargar_accion)

    def cargar_equipo():
        #Hacer inputs como una lista para cargarlo
        equipo = []

    def mostrar(self):
        self.label.pack()
