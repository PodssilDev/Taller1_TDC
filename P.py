
from cProfile import label
import tkinter as tk
from tkinter import BOTTOM, filedialog, Text
import os

#Listas de opciones
opciones1 = ["Duración corta","Duración Media","Duración Larga"]
opciones2 = ["Exponente","Underground"]
opciones3 = ["Moderna","Clasica"]
opciones4 = ["Cantante","Banda"]

#Listas que Contienen las opciones
Lista_suprema = [opciones1, opciones2, opciones3, opciones4]

Lista = ["Duración","Reconocimiento","Epoca","Cantante o Banda"]
Lista_de_entradas = []


def recivir():
    for clicked1 in Lista_de_entradas:
        print(str(clicked1.get()))
    print(entradas.get())

#La pantalla del Programa
root = tk.Tk()
root.geometry("1200x500")

#El fondo del programa
canvas = tk.Canvas(root , bg="#EA7600")
canvas.place(relwidth=1, relheight=1)

#lugar donde estan las opciones
frame = tk.Frame(root, bg="#002F6C")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Titulo de la encuesta
titulo = tk.Label(frame, text = "Prieba del Taller de TDC", bg="#B1B1B1" , width=67)
titulo.grid(padx=2 , pady=2, row = 0 , column = 0 , sticky=tk.E+tk.W)

#Nombre de que entrar en la encuesta
for i in range(len(Lista)):
    label1 = tk.Label(frame , text= Lista[i] , bg="#B1B1B1")
    primo = (2*i)+1
    label1.grid(padx=2 , pady=2, row = primo , column = 0 , sticky=tk.E+tk.W)

#las opciones que puedes eleguir en la encuesta
for i in range(len(Lista_suprema)):
    clicked1 = tk.StringVar()
    clicked1.set(Lista_suprema[i][0])
    abrir1 = tk.OptionMenu(frame, clicked1, *Lista_suprema[i])
    abrir1.grid(padx=2 , pady=2, row = (2*i)+2 , column = 0 , sticky=tk.E+tk.W)
    Lista_de_entradas.append(clicked1)

#etiqueta que nombra donde puedes escribir en la encuesta
label2 = tk.Label(frame, text="Pequeña descripcion de lo que quiere.", bg="#B1B1B1")
label2.grid(padx=2 , pady=2,row=(2*len(Lista))+3, columnspan=2 , sticky=tk.E+tk.W)

#entrada de la encuesta
entradas = tk.Entry(frame, justify="center")
entradas.grid(row=(2*len(Lista))+4, columnspan=2, ipadx=10, ipady=10 ,sticky=tk.E+tk.W)

#boton que guarda las encuesta
summit = tk.Button(frame, text="Summit", padx=10, pady=5, fg = "black", bg = "white", command=recivir)
summit.grid(padx=2 , pady=2,row=(2*len(Lista))+5, columnspan=2)


#aqui agrgar una funcion que cuando encuentre una respuesta la escriba sobre esto
salida_texto = "Salida"

salida= tk.Label(frame, text= salida_texto, bg = "white", width=67)
salida.grid( row=0, rowspan=(2*len(Lista))+5, column = 2, sticky=tk.N ,ipadx = 10,ipady = 10)


'''
def importar():
    conjunto = ""
    for algo in Lista_de_entradas:
        conjunto = conjunto + algo.get() + "\n"
        label2.config(text = conjunto)
    return None 

for i in range(len(Lista)):
    label1 = tk.Label(frame, text=Lista[i], bg="#B1B1B1")
    label1.grid(padx=2 , pady=2, row = i , column = 0 , sticky=tk.E+tk.W)

for i in range(len(Lista)):
    entradas = tk.Entry(frame, width=50)
    entradas.grid(padx=2 , pady=2 , row = i , column=1)
    Lista_de_entradas.append(entradas)

summit = tk.Button(frame, text="Summit", padx=10, pady=5, fg = "black", bg = "white", command=importar)
summit.grid(row=len(Lista)+1, columnspan=2)

label2 = tk.Label(frame, text="")
label2.grid(padx=2, pady=2, rowspan = len(Lista), column=2)
'''

'''
canvas = tk.Canvas(root, width=700, height=700, bg="#EA7600")
canvas.pack()

frame = tk.Frame(root, bg="#002F6C")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label1 = tk.Label(frame, text="Duración")
label1.pack(side="top")

Duración = tk.Entry(frame, width=50)
Duración.pack(side="top")

forma con hacerlo con columnas

label1 = tk.Label(frame, text="Duración", bg="#B1B1B1")
label1.grid(column=1, row=0)

vacio = tk.Label(frame, width=1, bg="#002F6C")
vacio.grid(column=0, row=0)

vacio2 = tk.Label(frame, width=1, bg="#002F6C")
vacio2.grid(column=2, row=0)

duration = tk.Entry(frame, width=50)
duration.grid(column=3, row=0)


label2 = tk.Label(frame, text="Duración")
label2.grid(column=1, row=1)

duration1 = tk.Entry(frame, width=50)
duration1.grid(column=3, row=1)
'''

'''
frame = tk.Frame(root, bg="#B1B1B1")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label1 = tk.Label(frame, text="Duracion")
label1.place(relx = 0.1,rely = 0.01)
duration = tk.Entry(frame, width=50)
duration.place(relx = 0.1, rely=0.01)
'''

root.mainloop()
