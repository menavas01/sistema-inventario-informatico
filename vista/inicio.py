from tkinter import ttk
from vista.cargar import CargarEquipo
from vista.asignacion import AsignacionEquipo
from vista.baja import BajaEquipo

class App ():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Inventario")  
        self.ventana.iconbitmap("assets/icon.ico")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)
        
        #Instancias de todas las pantallas
        self.inicio = Inicio(self.ventana, self)
        self.cargarEquipo = CargarEquipo(self.ventana)
        self.asignacionEquipo = AsignacionEquipo(self.ventana)
        self.bajaEquipo = BajaEquipo(self.ventana)
        
        self.inicio.mostrar_inicio()
        
    def mostrar_cargar_equipo(self):
        self.inicio.ocultar()
        self.cargarEquipo.mostrar_carga()
        self.volver = ttk.Button(text = "Volver", command = self.volver_carga, width = 50)
        self.volver.pack()
        
    def volver_carga(self):
        self.cargarEquipo.ocultar()
        self.inicio.mostrar_inicio()
        self.volver.pack_forget()
        
    def mostrar_asignacion_equipo(self):
        self.inicio.ocultar()
        self.asignacionEquipo.mostrar_asignacion()
        self.volver = ttk.Button(text = "Volver", command = self.volver_asignacion, width = 50)
        self.volver.pack()
        
    def volver_asignacion(self):
        self.asignacionEquipo.ocultar()
        self.inicio.mostrar_inicio()
        self.volver.pack_forget()
        
    def mostrar_baja_equipo(self):
        self.inicio.ocultar()
        self.bajaEquipo.mostrar_baja()
        self.volver = ttk.Button(text = "Volver", command = self.volver_baja, width = 50)
        self.volver.pack()
        
    def volver_baja(self):
        self.bajaEquipo.ocultar()
        self.inicio.mostrar_inicio()
        self.volver.pack_forget()

class Inicio():
    def __init__ (self, ventana, app):
        self.ventana = ventana
        self.app = app
        self.frame = ttk.Frame(self.ventana)
        
        self.label = ttk.Label (self.frame, text="¿Que accion desea realizar?", font = ("system-ui",11))
        
        self.carga = ttk.Button(self.frame, text="Cargar Equipo", command= self.cargar_equipo, width = 50)
        self.asignacion = ttk.Button(self.frame, text="Asignacion De Equipo", command= self.asignacion_equipo, width = 50)
        self.baja = ttk.Button(self.frame, text="Baja De Equipo", command= self.baja_equipo, width = 50)
        
    def mostrar_inicio(self):
        self.frame.pack()
        self.label.pack(padx = 10, pady = 10)
        self.carga.pack(padx = 10, pady = 10)
        self.asignacion.pack(padx = 10, pady = 10)
        self.baja.pack(padx = 10, pady = 10)
        
    def ocultar(self):
        self.frame.pack_forget()
    
    def cargar_equipo(self):
        self.ocultar()
        self.app.mostrar_cargar_equipo()
        
    def asignacion_equipo(self):
        self.ocultar()
        self.app.mostrar_asignacion_equipo()
        
    def baja_equipo(self):
        self.ocultar()
        self.app.mostrar_baja_equipo()