
import os
import tkinter as tk
from tkinter import messagebox


def Limpiar_Campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_fun():
    Limpiar_Campos()
def guardar_Valores():
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    genero = ""
    if var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get()==2:
        genero="Mujer"
    elif var_genero.get()==3:
        genero="Otro"

    carpeta = r"C:\Users\broth\Desktop\Practica04"
    os.makedirs(carpeta, exist_ok=True)

    with open(r"C:\Users\broth\Desktop\Practica04\FormularioPython.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellidos: {apellidos}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Estatura: {estatura}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Género: {genero}\n")

ventana = tk.Tk()
ventana.geometry ("520x500")
ventana.title("Fomulario Vr. 01")
ventana.configure(bg="lightblue")


var_genero = tk.IntVar()


lbNombre = tk.Label(ventana, text="Nombre (s):", font=("MS Comic Sans", 13))
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:", font=("MS Comic Sans", 13))
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono:", font=("MS Comic Sans", 13))
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:", font=("MS Comic Sans", 13))
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:", font=("MS Comic Sans", 13))
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Género:", font=("MS Comic Sans", 13))
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()
rbOtro=tk.Radiobutton(ventana, text="Otro", variable=var_genero, value=3)
rbOtro.pack()


btnBorrar = tk.Button(ventana, text="Borrar", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_Valores)
btnGuardar.pack()

ventana.mainloop()