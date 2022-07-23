from cgitb import text
import tkinter
from tkinter import filedialog
from tkinter import font
raiz = tkinter.Tk()
raiz.title("File Address")
#abrir fichero
def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir Archivo")
    #insertar ruta en la caja de texto
    entrada.insert(0,rutafichero)
      
boton = tkinter.Button(raiz,text="Buscar archivo",command=abrirfichero)
boton.pack()

entrada = tkinter.Entry(raiz)
entrada.config(width=100,justify="center")
entrada.pack()

raiz.mainloop()