import tkinter as tk
from tkinter import messagebox

#This will be the funtion that which let ass to press
#The bottom to say hello


def saludar():
    name = entry_name.get()
    if name.strip():
        messagebox.showinfo("Welcome", f"Hello {name} please click acept buton")
    else:
        messagebox.showwarning("Warning", "Please, type your name.")

#With this we create the main winwow or the GUI
ventana = tk.Tk()
ventana.title("Program that say hello")
ventana.geometry("300x150")
ventana.configure(bg="#f0f0f0")

#We define entry name
entry_name = tk.Entry(ventana, width=30)
entry_name.pack(pady=5)

#Etiquete
label = tk.Label(ventana, text="Please type your name:", bg="#f0f0f0", font=("Arial", 10))
label.pack(pady=5)

#Hello button

boton_saludar = tk.Button(ventana, text="hello", command=saludar, bg="#4caf50", fg="white")
boton_saludar.pack(pady=5)

#exit buttom
buton_exit = tk.Button(ventana, text="exit", command=ventana.quit, bg="#4caf50", fg="white")
buton_exit.pack(pady=5)

ventana.mainloop()



