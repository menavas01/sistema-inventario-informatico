from tkinter import ttk
from ddbb.consultas_ddbb import obtener_equipo
from tkcalendar import DateEntry

class AsignacionEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frame = ttk.Frame(self.ventana)

        self.label = ttk.Label (self.frame, text = "Asignar equipo", font = ("system-ui",11))
        
        equipos = obtener_equipo()
        self.tipoEquipo = ttk.Combobox(self.frame, state = "readonly", values = equipos)
        self.tipoEquipo.set("Selecciona una opcion")
        
        self.usuario = ttk.Entry(self.frame)
        self.motivo = ttk.Entry(self.frame)
        self.responsable = ttk.Entry(self.frame)
        self.area = ttk.Entry(self.frame)
        self.fecha = DateEntry(self.frame, date_pattern = "dd/mm/yyyy")

        self.asignar = ttk.Button(self.frame, text = "Asignar", command = self.asignacion_equipos)

    def asignacion_equipos(self):
        print ("Equipo asignado")

    def mostrar_asignacion(self):
        self.frame.pack()
        self.label.pack(padx= 10, pady= 10)
        self.tipoEquipo.pack(padx= 10, pady= 10)
        self.usuario.pack(padx= 10, pady= 10)
        self.motivo.pack(padx= 10, pady= 10)
        self.responsable.pack(padx= 10, pady= 10)
        self.area.pack(padx= 10, pady= 10)
        self.fecha.pack(padx= 10, pady= 10)
        self.asignar.pack(padx= 10, pady= 10)
        
    def ocultar(self):
        self.frame.pack_forget()