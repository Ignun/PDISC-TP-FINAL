from tkinter import *

ventana = Tk()
ventana.title("Lector Hexadecimal de archivos")
ventana.geometry('500x500')

Input = StringVar()

Entry(ventana, textvariable=Input).place(x=10, y=20)
Label(ventana, text="Ingrese la Direccion absoluta del archivo").place(x=10, y=1)

def subir():
    print(Input.get())
    with open(Input.get(), "rb") as file:
        listado = " ".join(map("{:02X}".format, file.read()))
        lista.insert(END, listado)

Button(ventana, text="Subir", command=subir).place(x=150, y=20)

lf = LabelFrame(ventana, text="Contenido Hexadecimal", fg="blue")
lf.place(x=10, y=50)
lista = Text(lf, width=60)
lista.pack()

ventana.mainloop()