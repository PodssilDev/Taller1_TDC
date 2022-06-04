# BLOQUE DE DEFINICIONES
# BLOQUE DE IMPORTACIONES
import sys
from pyswip import Prolog
from statistics import mode
from cProfile import label
import tkinter as tk
from tkinter import BOTTOM, filedialog, Text
import os

#Bloque de Listas
#----------------------------------------------------------------------------
#Listas de opciones
opciones1 = ["Exponente","Underground"]
opciones2 = ["Duración Corta","Duración Normal","Duración Larga"]
opciones3 = ["Decada Moderna","Los 2000s","Los 90s","Los 80s","Los 70s","Clasica"]
opciones4 = ["Solista","Banda"]
opciones5 = ["Que tenga letras de amor"
            ,"Que tenga guitarras fuertes y distorcionadas"
            ,"Que tenga una preferencia por la artesania y diversos elementos"
            ,"Que tenga sonidos electronicos"
            ,"Que provoque querer bailar"
            ,"Que contenga una letra hablada rapidamente"
            ,"Que tenga una letra en tono medio y una guitarra electronica"
            ,"Que tenga sonidos de saxophone"
            ,"Que tenga sonidos de una bateria ritmica"
            ,"Que tenga ritmos bastante movidos"
            ,"Que tenga sinfonia y tengan poca o nula improvisacion"
            ,"Que tenga tempo rapido y sonidos distorcionados"
            ,"Que use el patron ritmico del son cubano"
            ,"Que tenga un ritmo de musica bailable y frenetico"
            ,"Que tenga tecnicas expresivas de la guitarra y harmonia"
            ,"Que emplee armonias vocales"
            ,"Ninguna de las anteriores"]


#Listas que Contienen las opciones
Lista_suprema = [opciones1, opciones2, opciones3, opciones4, opciones5]

Lista = ["Reconocimiento","Duración","Epoca","Cantante o Banda","Caracteristicas Extras"]
Lista_de_entradas = []
#----------------------------------------------------------------------------

# BLOQUE DE FUNCIONES
#----------------------------------------------------------------------------

def reconocer_caracteristica(caso):
    match caso:
        case "Que tenga letras de amor": # Romantica
            return "letras_de_amor"

        case "Que tenga guitarras fuertes y distorcionadas": # Metal
            return "guitarras_fuertes_distorcionadas"

        case "Que tenga una preferencia por la artesania y diversos elementos": # POp
            return "artesania_diversos_elementos" 

        case "Que tenga sonidos electronicos": # Electronica
            return "sonidos_electronicos"

        case "Que provoque querer bailar": # Disco
            return "querer_bailar"

        case "Que contenga una letra hablada rapidamente": #Hip-Hop
            return "letras_rapidas"

        case "Que tenga una letra en tono medio y una guitarra electronica": # Rock
            return "tono_medio_guitarra"

        case "Que tenga sonidos de saxophone": # Jazz
            return "sonidos_saxophone"

        case "Que tenga sonidos de una bateria ritmica": # Reggae
            return "sonidos_bateria" 

        case "Que tenga ritmos bastante movidos": #  Cumbia
            return "ritmos_movidos"

        case "Que tenga sinfonia y tengan poca o nula improvisacion": # Clasica
            return "sinfonia"

        case "Que tenga tempo rapido y sonidos distorcionados": # Tecno
            return "tempo_rapido"

        case "Que use el patron ritmico del son cubano": # Salsa
            return "patron_cubano"

        case "Que tenga un ritmo de musica bailable y frenetico": # Rock n Roll
            return "ritmo_bailable_frenetico"

        case "Que tenga tecnicas expresivas de la guitarra y harmonia":
            return "tecnicas_expresivas" # Blues

        case "Que emplee armonias vocales": # Country
            return "armonias_vocales"

        case "Ninguna de las anteriores":
            return "_"

def reconocer_tipo_artista(caso):
    match caso:
        case "Exponente":
            return "exponente"

        case "Underground":
            return "underground"

def reconocer_decada(caso):
    match caso:
        case "Decada Moderna":
            return "moderna"

        case "Los 2000s":
            return "dosmil"

        case "Los 90s":
            return "noventas"

        case "Los 80s":
            return "ochentas"

        case "Los 70s":
            return "setentas"

        case "Clasica":
            return "antigua"

def reconocer_duracion(caso):
    match caso:
        case "Duración Corta":
            return "corta"

        case "Duración Normal":
            return "normal"

        case "Duración Larga":
            return "larga"

def reconocer_solista_banda(caso):
    match caso:
        case "Solista":
            return "solista"

        case "Banda":
            return "banda"

def recivir():
    listbox.delete(0,tk.END)
    Lista_de_salida = []
    for clicked1 in Lista_de_entradas:
        Lista_de_salida.append(clicked1.get())
    #Lista_de_salida.append(entradas.get())
    print(Lista_de_salida)
    tipo_artista = reconocer_tipo_artista(Lista_de_salida[0])
    duracion = reconocer_duracion(Lista_de_salida[1])
    decada = reconocer_decada(Lista_de_salida[2])
    solista_banda = reconocer_solista_banda(Lista_de_salida[3])
    caracteristicas_extras = reconocer_caracteristica(Lista_de_salida[4])
    resultados = songQuery(tipo_artista, duracion, decada, solista_banda, caracteristicas_extras)
    i = 0
    listbox.insert(tk.END, "Resultados: ")
    listbox.insert(tk.END, "Su genero preferido es: " + resultados[0]["Genero"].upper())
    listbox.insert(tk.END, "Canciones recomendadas: ")
    listbox.insert(tk.END, "")
    for i in range(len(resultados)):
        listbox.insert(tk.END,str(i+1)+". : " +  resultados[i]["Cancion"].decode("utf-8"))
        i += 1



def mas_repetido(lista_generos):
    return(mode(lista_generos))

def songQuery(tipo_artista, duracion, decada, banda_solista, caracteristicas_extras):
    return list(prolog.query("song(Cancion, Genero," + tipo_artista + "," + duracion + "," + decada + ","  + banda_solista + "," + caracteristicas_extras +")"))
# lista_respuestas = list(prolog.query("song(Cancion,Genero," + tipo_artista + "," + duracion + "," + moderna_antigua + "," + solitario_grupo + ")"))

def generoMasRepetido(respuestas):
    return mode([r["Genero"] for r in respuestas])

def cancionesGenero(respuestas, genero):
    return [r["Cancion"] for r in respuestas if r["Genero"] == genero]

def gustosSimilares(datos):
    respuestas = []
    for i in range(0, len(datos)):
        if(respuestas != []):
            return respuestas
        d = datos
        d[i] = "_"      
        respuestas = songQuery(d[0], d[1], d[2], d[3])

def entrega_cancion(V, Genero, lista_cancion):
    if(V):
        entrega = "El Genero Encontrado: " + Genero +"\n"
        for i in range(lista_cancion):
            entrega = entrega +  str(i+1) + ".-" + lista_cancion[i] + "\n" 
    else:
        entrega = "No se encontraron preferencias, pero se recomienda el genero: " + Genero + "\n"
        for i in range(lista_cancion):
            entrega = entrega + str(i+1) + ".-" + lista_cancion[i] + "\n" 
    return entrega

#----------------------------------------------------------------------------

# BLOQUE PRINCIPAL
prolog = Prolog()
prolog.consult("base.pl")

datos = songQuery("exponente", "normal", "moderna", "banda", "tono_medio_guitarra")
print(datos)

root = tk.Tk()
root.geometry("1200x500")
root.config(bg = "#1a9e8f")
listbox = tk.Listbox(root)
listbox.place(relx = 0.01, rely = 0.1, relwidth = 0.7, relheight= 0.7)
clicked1 = tk.StringVar()
clicked1.set(Lista_suprema[0][0])
abrir1 = tk.OptionMenu(root, clicked1, *Lista_suprema[0])
abrir1.place(relx=0.05,rely=0.85)
Lista_de_entradas.append(clicked1)
clicked2 = tk.StringVar()
clicked2.set(Lista_suprema[1][0])
abrir2 = tk.OptionMenu(root, clicked2, *Lista_suprema[1])
abrir2.place(relx=0.15,rely=0.85)
Lista_de_entradas.append(clicked2)
clicked3 = tk.StringVar()
clicked3.set(Lista_suprema[2][0])
abrir3 = tk.OptionMenu(root, clicked3, *Lista_suprema[2])
abrir3.place(relx=0.27,rely=0.85)
Lista_de_entradas.append(clicked3)
clicked4 = tk.StringVar()
clicked4.set(Lista_suprema[3][0])
abrir4 = tk.OptionMenu(root, clicked4, *Lista_suprema[3])
abrir4.place(relx=0.40,rely=0.85)
Lista_de_entradas.append(clicked4)
clicked5 = tk.StringVar()
clicked5.set(Lista_suprema[4][0])
abrir5 = tk.OptionMenu(root, clicked5, *Lista_suprema[4])
abrir5.place(relx=0.49,rely=0.85)
Lista_de_entradas.append(clicked5)

text1 = tk.Label(root, text = "Bienvenido al buscador de canciones.", bg = "#1a9e8f", fg = "white", font = 10)
text1.place(relx = 0.01, rely = 0.03)
text2 = tk.Label(root, text = "Seleccione sus preferencias y gustos.", bg = "#1a9e8f", fg = "white", font = 10)
text2.place(relx = 0.3, rely = 0.03)
boton = tk.Button(root, text="Buscar canciones", command = lambda:recivir())
boton.place(relx = 0.80, rely = 0.50)

barra = tk.Scrollbar(root, command = listbox.yview)
barra.place(relx = 0.71, rely = 0.10)
root.mainloop()

'''
canvas = tk.Canvas(root , bg="#D9D8D7")
canvas.place(relwidth=1, relheight=1)
text = tk.Label(canvas, text = "Bienvenido a la aplicación de musica", font=("Arial Black", 20), bg="#D9D8D7")
text.place(relx=0.5, rely=0.1, anchor="s")
frame = tk.Frame(root, bg="#4a7abc")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titulo = tk.Label(frame, text = "Responda las preguntas basandose en sus gustos", bg="#B1B1B1" , width=67)
titulo.grid(padx=2 , pady=2, row = 0 , column = 0 , sticky=tk.E+tk.W)

#Nombre de que entrar en la encuesta
for i in range(len(Lista)):
    label1 = tk.Label(frame , text= Lista[i] , bg="#fff")
    primo = (2*i)+1
    label1.grid(padx=2 , pady=2, row = primo , column = 0 , sticky=tk.E+tk.W)

#las opciones que puedes eleguir en la encuesta
for i in range(len(Lista_suprema)):
    clicked1 = tk.StringVar()
    clicked1.set(Lista_suprema[i][0])
    abrir1 = tk.OptionMenu(frame, clicked1, *Lista_suprema[i])
    abrir1.grid(padx=2 , pady=2, row = (2*i)+2 , column = 0 , sticky=tk.E+tk.W)
    Lista_de_entradas.append(clicked1)

summit = tk.Button(frame, text="Summit", padx=10, pady=5, fg = "black", bg = "white", command=recivir)
summit.grid(padx=2 , pady=2,row=(2*len(Lista))+4, columnspan=2)

root.mainloop()
'''
'''
respuesta_1 = input("¿Prefiere un artista Exponente o Underground?: ")
respuesta_2 = input("¿Prefiere una cancion larga, corta o normal?: ")
respuesta_3 = input("¿Prefiere una cancion de antes o despues de la decada de los 2000?:")
respuesta_4 = input("¿Prefiere una banda o un cantante en solitario?:")
respuesta_5 = input("¿Prefiere una cancion con alguna caracteristica especifica?: ")

no_encontrado = False # Se va a utilizar para el caso alternativo

if respuesta_1 == "exponente":
    tipo_artista = "exponente"
else:
    tipo_artista = "underground"

if respuesta_2 == "corta":
    duracion = "corta"

elif respuesta_2 == "normal":
    duracion = "normal"

else:
    duracion = "larga"

if respuesta_3 == "antigua": # Moderna, Dosmil, Noventas, Ochentas, Setentas, Clasica
    moderna_antigua = "antigua"

else:
    moderna_antigua = "moderna"

if respuesta_4 == "banda":
    solitario_grupo = "banda"
else:
    solitario_grupo = "cantante"
'''

'''

# Consulta principal. Se buscan aquellas canciones que correspondan a las caracteristicas
# elegidas por el usuario.

lista_respuestas = list(prolog.query("song(Cancion,Genero," + tipo_artista + "," + duracion + "," + moderna_antigua + "," + solitario_grupo + ")"))

# Es posible que no se encuentren resultados. En ese caso, se buscan canciones con 
# caracteristicas similares (Utilizando variables anonimas)

if(lista_respuestas == []):
    no_encontrado = True
    lista_respuestas = list(prolog.query("song(Cancion,Genero," + "_" + "," + duracion + "," + moderna_antigua + "," + solitario_grupo +")"))
    if(lista_respuestas == []):
        lista_respuestas = list(prolog.query("song(Cancion,Genero," + tipo_artista + "," + "_" + "," + moderna_antigua + "," + solitario_grupo +")"))
        if(lista_respuestas == []):
            no_encontrado = True
            lista_respuestas = list(prolog.query("song(Cancion,Genero," + tipo_artista + "," + duracion + "," + "_" + "," + solitario_grupo +")"))
            if(lista_respuestas == []):
                no_encontrado = 1
                lista_respuestas = list(prolog.query("song(Cancion,Genero," + tipo_artista + "," + duracion + "," + moderna_antigua + "," + "_" +")"))

lista_generos = []
if lista_respuestas == []:
    print("No hay respuestas")
else:
    if(no_encontrado == True):
        print("No se encontraron canciones con las caracteristicas elegidas, pero los siguientes son similares: ")
    else:
        print("Se encontraron las siguientes canciones: ")
    for respuesta in lista_respuestas:
        lista_generos.append(respuesta["Genero"])
        print(respuesta["Cancion"],"|", respuesta["Genero"])

print(mas_repetido(lista_generos))


#BLoque de la aplicación
#--------------------------------------------------------------------------------------

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
titulo = tk.Label(frame, text = "Prueba del Taller de TDC", bg="#B1B1B1" , width=67)
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


#entrada de la encuesta ahora no utilizada
'''

# entradas = tk.Entry(frame, justify="center")
# entradas.grid(row=(2*len(Lista))+4, columnspan=2, ipadx=10, ipady=10 ,sticky=tk.E+tk.W)
'''

#boton que guarda las encuesta
summit = tk.Button(frame, text="Summit", padx=10, pady=5, fg = "black", bg = "white", command=recivir)
summit.grid(padx=2 , pady=2,row=(2*len(Lista))+4, columnspan=2)


#aqui agrgar una funcion que cuando encuentre una respuesta la escriba sobre esto

#salida_texto = entrega_cancion(no_encontrado, Genero, Lista_canciones) #modificar para que entrege listo el texto 
salida_texto = "Salida"

salida= tk.Label(frame, text= salida_texto, bg = "white", width=67)
salida.grid( row=0, rowspan=(2*len(Lista))+5, column = 2, sticky=tk.N ,ipadx = 10,ipady = 10)

root.mainloop()
#----------------------------------------------------------------------------
# Primero realizar las consultas, procurarse que funcione sin interfaz (LISTO)
# Luego, realizar las consultas con interfaz (PENDIENTE)
'''