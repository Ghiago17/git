import tkinter as tk
import tkinter.messagebox as messagebox

def registrar():
    info = f"nonbre: {entrada_nombre.get()}\napellido: {entrada_apellido.get()}\nEdad: {entrada_edad.get()}\ndireccion: {entrada_direccion.get()}\nnumero: {entrada_telefono.get()}\nSexo: {sexo.get()}\nCiudad: {ciudades[listbox_ciudad.curselection()[0]]}"
    messagebox.showinfo("Información del Registro", info)

ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.config(bg="#f7dc6f")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)       
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.grid(row=1, column=1)

tk.Label(ventana, text="Edad:").grid(row=2, column=0)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=2, column=1)

tk.Label(ventana, text="Dirección:").grid(row=3, column=0)
entrada_direccion = tk.Entry(ventana)
entrada_direccion.grid(row=3, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=4, column=0)
entrada_telefono = tk.Entry(ventana)
entrada_telefono.grid(row=4, column=1)

sexo = tk.StringVar()
tk.Label(ventana, text="Sexo:").grid(row=5, column=0)
tk.Radiobutton(ventana, text="Masculino", variable=sexo, value="Masculino").grid(row=5, column=1)
tk.Radiobutton(ventana, text="Femenino", variable=sexo, value="Femenino").grid(row=5, column=2)


tk.Label(ventana, text="Ciudad:").grid(row=6, column=0)
ciudades = ["perreira", "cucuta", "cartagena"]
listbox_ciudad = tk.Listbox(ventana, selectmode=tk.SINGLE, height=len(ciudades))
for ciudad in ciudades:
    listbox_ciudad.insert(tk.END, ciudad)
listbox_ciudad.grid(row=6, column=1)

tk.Button(ventana, text="Registrar", command=registrar).grid(row=7, column=0, columnspan=2)

ventana.mainloop()