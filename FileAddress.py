from cgitb import text
import tkinter
from tkinter import filedialog
from tkinter import font
from tkinter import *
raiz = tkinter.Tk()
raiz.title("File Address")
#se agrega el icono de la ventana
img = PhotoImage(file='C:\\Users\\BetinBracamontes\\OneDrive - Universidad del Magdalena\\2022\\PYTHON\\FileAddress\\cadena.png')
raiz.iconphoto(False,img)
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