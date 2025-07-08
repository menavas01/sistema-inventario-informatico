import tkinter as tk
from vista.vista import CargarEquipo

def  main():  
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')  
    ventana.iconbitmap('assets/icon.ico')
    ventana.geometry("680x430")

    app = CargarEquipo(ventana)
    app.mostrar()

    ventana.mainloop()

if __name__ == '__main__':
    main()