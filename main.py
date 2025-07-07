import tkinter as tk
from tkinter import ttk
from ddbb.ddbb import listar_equipos, Conexion

def  main():  
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')  
    ventana.iconbitmap('assets/icon.ico')
    
    main_frame = tk.Frame(ventana)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    equipos = listar_equipos()
    
    headers = ["ID Equipo", "Serie", "Marca", "Modelo", "Tipo"]
    for col, header in enumerate(headers):
        tk.Label(scrollable_frame, 
        text=header,
        font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15, anchor="center").grid(row=0, column=col, padx=1, pady=1)

    ventana.mainloop()

if __name__ == '__main__':
    main()