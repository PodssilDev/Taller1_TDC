
from cProfile import label
import tkinter as tk
from tkinter import BOTTOM, filedialog, Text
import os
Lista = ["Duracion", "genero", "ETC"]
Lista_de_entradas = []

def importar():
    conjunto = ""
    for algo in Lista_de_entradas:
        conjunto = conjunto + algo.get() + "\n"
        label2.config(text = conjunto)
    return None 

root = tk.Tk()
root.geometry("600x500")

canvas = tk.Canvas(root , bg="#EA7600")
canvas.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#002F6C")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


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
