import tkinter as tk
from vista.inicio import App

def  main():  
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()

if __name__ == '__main__':
    main()