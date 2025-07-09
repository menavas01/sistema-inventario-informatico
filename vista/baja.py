from tkinter import ttk
from ddbb.consultas_ddbb import obtener_equipo
from tkcalendar import DateEntry

class BajaEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Baja equipo", font = ("system-ui",11))
        
        equipos = obtener_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = equipos)
        self.tipoEquipo.set("Selecciona una opcion")
        
        self.motivo = ttk.Entry(self.frame)
        self.fecha = DateEntry(self.frame, date_pattern = "dd/mm/yyyy")

        self.baja = ttk.Button(self.frame, text = "Dar de baja", command = self.baja_equipos)

    def baja_equipos(self):
        print ("Equipo bajado")

    def mostrar_baja(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.tipoEquipo.pack(padx= 10, pady= 10)
        self.motivo.pack(padx= 10, pady= 10)
        self.fecha.pack(padx= 10, pady= 10)
        self.baja.pack(padx= 10, pady= 10)
        
    def ocultar(self):
        self.frame.pack_forget()