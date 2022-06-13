# Taller 1 - Grupo 3
# Autores: Mastias Figueroa, Daniel Frez, Javier Sanhueza y John Serrano
# Teoria de la Computacion 2022-1

# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------

from pyswip import Prolog # Importamos Prolog
from statistics import mode # Importamos mode para obtener la moda de una lista
import tkinter as tk # Importamos Tkinter para la interfaz grafica

# DEFINICIONES DE FUNCIONES
#----------------------------------------------------------------------------

'''
Entrada: Una caracteristica extra (string) de una musica.
Salida: Un string de la caracteristica en forma abreviada.
Descripcion: Funcion que permite reconocer la caracteristica extra de una musica
y entregar la caracteristica de forma abreviada para poder buscarla en la base de
conocimientos.
'''
def reconocer_caracteristica(caso):
    match caso:
        case "Que tenga letras de amor": # Romantica
            return "letras_de_amor"

        case "Que tenga guitarras fuertes y distorcionadas": # Metal
            return "guitarras_fuertes_distorcionadas"

        case "Que tenga una preferencia por la artesania y diversos elementos": # Pop
            return "artesania_diversos_elementos" 

        case "Que tenga sonidos electronicos": # Electronica
            return "sonidos_electronicos"

        case "Que provoque querer bailar": # Disco
            return "querer_bailar"

        case "Que contenga una letra hablada rapidamente": # Hip-Hop
            return "letras_rapidas"

        case "Que tenga una letra en tono medio y una guitarra electronica": # Rock
            return "tono_medio_guitarra"

        case "Que tenga sonidos de saxophone": # Jazz
            return "sonidos_saxophone"

        case "Que tenga sonidos de una bateria ritmica": # Reggae
            return "sonidos_bateria" 

        case "Que tenga ritmos bastante movidos": # Cumbia
            return "ritmos_movidos"

        case "Que tenga sinfonia y tengan poca o nula improvisacion": # Clasica
            return "sinfonia"

        case "Que tenga tempo rapido y sonidos distorcionados": # Techno
            return "tempo_rapido"

        case "Que use el patron ritmico del son cubano": # Salsa
            return "patron_cubano"

        case "Que tenga un ritmo de musica bailable y frenetico": # Rock n Roll
            return "ritmo_bailable_frenetico"

        case "Que tenga tecnicas expresivas de la guitarra y harmonia": # Blues
            return "tecnicas_expresivas" 

        case "Que emplee armonias vocales": # Country
            return "armonias_vocales"

        case "Ninguna de las anteriores":
            return "_"

'''
Entrada: Un reconocimiento de un artista (string).
Salida: Un string del reconocimiento en forma abreviada.
Descripcion: Funcion que permite reconocer el reconocimiento de un artista, 
es decir, si es exponente o underground. Entrega un string que permite buscar
la caracteristica en la base de conocimientos.
'''
def reconocer_tipo_artista(caso):
    match caso:
        case "Exponente": # Exponente
            return "exponente"

        case "Underground": # Underground
            return "underground"
        
        case "No estoy seguro": # Caso por defecto
            return "exponente"
'''
Entrada: Una epoca de una musica (string).
Salida: Un string de la epoca en forma abreviada.
Descripcion: Funcion que permite reconocer la epoca de una musica. Entrega un 
string que permite buscar la caracteristica en la base de conocimientos.
'''
def reconocer_decada(caso):
    match caso:
        case "Decada Moderna": # Decada Moderna (2010 en adelante)
            return "moderna"

        case "Los 2000s": # Decada de los 2000s
            return "dosmil"

        case "Los 90s": # Decada de los 90s
            return "noventas"

        case "Los 80s": # Decada de los 80s
            return "ochentas"

        case "Los 70s": # Decada de los 70s
            return "setentas"

        case "Clasica": # Decadas desde la antiguedad hacia los 60s
            return "antigua"

'''
Entrada: Una duracion de una musica (string).
Salida: Un string de la duracion en forma abreviada.
Descripcion: Funcion que permite reconocer la duracion de una musica. Entrega un
string que permite buscar la caracteristica en la base de conocimientos.
'''
def reconocer_duracion(caso):
    match caso:
        case "Duración Corta": # Duracion de menos de 3 minutos
            return "corta"

        case "Duración Normal": # Duracion entre 3 y 4 minutos
            return "normal"

        case "Duración Larga": # Duracion de mas de 4 minutos
            return "larga"

'''
Entrada: Un string que representa si el arista es un solista o una banda.
Salida: Un string que representa si el arista es un solista o una banda.
Descripcion: Funcion que permite reconocer si el arista es un solista o una banda,
entrega un string que es utilizado para buscar la caracteristica en la base de conocimientos.
'''
def reconocer_solista_banda(caso):
    match caso:
        case "Solista": # Artista Solista / Cantante
            return "solista"

        case "Banda": # Artista Banda / Grupo
            return "banda"

'''
Entrada: No tiene entrada
Salida: No tiene salida como tal, pero escribe cosas en la interfaz grafca
Descripcion: Funcion principal que permite realizar el proceso de busqueda en la 
base de conocimientos y escribir los resultados encontrados en la interfaz grafica. 
'''
def recivir():
    listbox.delete(0,tk.END) # Se limpia el listbox cada vez que se buscan nuevos resultados
    no_encontrado = False # Se inicializa la variable que indica si se encontro algo o no
    lista_de_salida = [] # Se inicializa la lista de salida de los resultados
    for clicked1 in lista_de_entradas: # Se recorre la lista de entradas
        lista_de_salida.append(clicked1.get()) # Se agregan las entradas a la lista de salida

    tipo_artista = reconocer_tipo_artista(lista_de_salida[0]) # Se obtiene el tipo de artista
    duracion = reconocer_duracion(lista_de_salida[1]) # Se obtiene la duracion
    decada = reconocer_decada(lista_de_salida[2]) # Se obtiene la decada
    solista_banda = reconocer_solista_banda(lista_de_salida[3]) # Se obtiene si es solista o banda
    # Se obtiene las caracteristicas extras
    caracteristicas_extras = reconocer_caracteristica(lista_de_salida[4])
    # Se realiza la consulta principal

    resultados = songQuery(tipo_artista, duracion, decada, solista_banda, caracteristicas_extras)
    if(resultados == []): # Si es que no se encontraron resultados
        # Se realiza una busqueda de resultados similares, sin considerar alguna caracteristica en especifico
        resultados = gustosSimilares([tipo_artista, duracion, decada, solista_banda, caracteristicas_extras])
        no_encontrado = True; # Debido a lo anterior, no_encontrado se declara como True
    listbox.insert(tk.END, "Resultados: ") # Se agrega una linea al listbox
    # Se agrega el genero preferido al listbox
    listbox.insert(tk.END, "Su genero preferido es: " + generoMasRepetido(resultados).upper())
    listbox.insert(tk.END, "") # Se agrega una linea al listbox
    if(no_encontrado == False): # Si no_encontrado es falso
        listbox.insert(tk.END, "Canciones recomendadas: ") # Se agrega una linea al listbox
    else:
        listbox.insert(tk.END, "No se encontraron canciones que se acomoden a sus gustos, pero se recomiendan las siguientes canciones: ")
    for i in range(len(resultados)): # Se recorre la lista de resultados
        # Se agregan todas las canciones encontradas junto con su genero correspondiente
        listbox.insert(tk.END,str(i+1)+". : " +  resultados[i]["Cancion"].decode("utf-8") + " | " + resultados[i]["Genero"].upper())

'''
Entrada: Cinco strings, donde el primero representa si el artista es un exponente o underground, el segundo la duracion de la cancion,
el segundo la duracion de la cancion, el tercero la decada de la cancion, el cuarto si es
que el artista es un solista o una banda, y el quinto la caracteristica extra.
Salida: Retorna una lista que contiene todas las coincidencias encontradas.
Descripcion: Funcion que permite buscar en la base de conocimientos las canciones que 
se acomoden a los parametros entregados. Entrega una lista de todas aquellas canciones que
cumplan con las caracteristicas entregadas.
'''
def songQuery(tipo_artista, duracion, decada, banda_solista, caracteristicas_extras):
    # Se realiza la consulta a la base de conocimientos
    return list(prolog.query("song(Cancion, Genero," + tipo_artista + "," + duracion + "," + decada + ","  + banda_solista + "," + caracteristicas_extras +")"))

'''
Entrada: Una lista de respuestas de musicas.
Salida: Un string que representa el genero mas repetido en la lista de respuestas.
Descripcion: Funcion que permite determinar el genero mas repetido en la lista de 
respuestas.
'''
def generoMasRepetido(respuestas):
    # Se retorna el genero mas repetido en la lista de respuestas
    return mode([r["Genero"] for r in respuestas])

'''
Entrada: Una lista de datos de musicas.
Salida: Una lista que contiene las musicas que se acomoden a los gustos del usuario.
Descripcion: Funcion que permite determinar las canciones que se acomoden a los gustos 
del usuario, buscando musicas con caracteristicas similares a las entregadas.
'''
def gustosSimilares(datos):
    respuestas = [] # Se inicializa la lista de respuestas
    for i in range(0, len(datos) - 1): # Se recorre la lista de datos
        if(respuestas != []): # Si se encontraron respuestas, se retorna la lista de respuestas
            return respuestas
        datos_2 = datos.copy() # Se copia la lista de datos a la variable datos_2
        datos_2[i] = "_" # Se cambia el dato de la lista de datos_2 por una variable anonima (_)
        # Se realiza la consulta a la base de conocimientos
        respuestas = songQuery(datos_2[0], datos_2[1], datos_2[2], datos_2[3], datos_2[4])

    for i in range(0, len(datos) - 1): # Se recorre la lista de datos
        if(respuestas != []): # Si se encontraron respuestas, se retorna la lista de respuestas
            return respuestas
        data_2 = datos # Se copia la lista de datos a la variable data_2
        data_2[i] = "_" # Se cambia el dato de la lista de datos_2 por una variable anonima (_)
        # Se realiza la consulta a la base de conocimientos
        respuestas = songQuery(data_2[0], data_2[1], data_2[2], data_2[3], data_2[4])

# BLOQUE PRINCIPAL
#----------------------------------------------------------------------------

#Listas de opciones a elegir en la interfaz grafica
opciones1 = ["Exponente","Underground", "No estoy seguro"] # Reconocimiento Artista
opciones2 = ["Duración Corta","Duración Normal","Duración Larga"] # Duracion
opciones3 = ["Decada Moderna","Los 2000s","Los 90s","Los 80s","Los 70s","Clasica"] # Decada
opciones4 = ["Solista","Banda"] # Solitario o Banda
opciones5 = ["Que tenga letras de amor" # Caracteristicas extras
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
#Lista que contiene las opciones
lista_suprema = [opciones1, opciones2, opciones3, opciones4, opciones5]
lista_de_entradas = [] # Lista que contiene las entradas de los usuarios

prolog = Prolog() # Inicializacion de Prolog
prolog.consult("base.pl") # Se consulta en la base de conocimientos

root = tk.Tk() # Se inicia la ventana de la interfaz
root.title("Buscador de canciones") # Se cambia el nombre del titulo de la ventana
root.geometry("1200x500") # Se cambia el tamaño de la ventana
root.config(bg = "#1a9e8f") # Se cambia el fondo de la ventana

listbox = tk.Listbox(root) # Se crea una Listbox, donde se escribiran los resultados
listbox.place(relx = 0.01, rely = 0.1, relwidth = 0.7, relheight= 0.7) # Se ajusta el tamaño y posicionamiento de la listbox

clicked1 = tk.StringVar() # Se crea una variable para guardar la opcion elegida en el primer menu
clicked1.set(lista_suprema[0][0]) # Se asigna un valor inicial a la variable
abrir1 = tk.OptionMenu(root, clicked1, *lista_suprema[0]) # Se crea un menu de opciones para el primer menu
abrir1.place(relx=0.03,rely=0.85) # Se ajusta el tamaño y posicionamiento del primer menu
lista_de_entradas.append(clicked1) # Se agrega la opcion elegida a la lista de entradas

clicked2 = tk.StringVar() # Se crea una variable para guardar la opcion elegida en el segundo menu
clicked2.set(lista_suprema[1][0]) # Se asigna un valor inicial a la variable
abrir2 = tk.OptionMenu(root, clicked2, *lista_suprema[1]) # Se crea un menu de opciones para el segundo menu
abrir2.place(relx=0.15,rely=0.85) # Se ajusta el tamaño y posicionamiento del segundo menu
lista_de_entradas.append(clicked2) # Se agrega la opcion elegida a la lista de entradas

clicked3 = tk.StringVar() # Se crea una variable para guardar la opcion elegida en el tercer menu
clicked3.set(lista_suprema[2][0]) # Se asigna un valor inicial a la variable
abrir3 = tk.OptionMenu(root, clicked3, *lista_suprema[2]) # Se crea un menu de opciones para el tercer menu
abrir3.place(relx=0.27,rely=0.85) # Se ajusta el tamaño y posicionamiento del tercer menu
lista_de_entradas.append(clicked3) # Se agrega la opcion elegida a la lista de entradas

clicked4 = tk.StringVar() # Se crea una variable para guardar la opcion elegida en el cuarto menu
clicked4.set(lista_suprema[3][0]) # Se asigna un valor inicial a la variable
abrir4 = tk.OptionMenu(root, clicked4, *lista_suprema[3]) # Se crea un menu de opciones para el cuarto menu
abrir4.place(relx=0.40,rely=0.85) # Se ajusta el tamaño y posicionamiento del cuarto menu
lista_de_entradas.append(clicked4) # Se agrega la opcion elegida a la lista de entradas

clicked5 = tk.StringVar() # Se crea una variable para guardar la opcion elegida en el quinto menu
clicked5.set(lista_suprema[4][0]) # Se asigna un valor inicial a la variable
abrir5 = tk.OptionMenu(root, clicked5, *lista_suprema[4]) # Se crea un menu de opciones para el quinto menu
abrir5.place(relx=0.49,rely=0.85) # Se ajusta el tamaño y posicionamiento del quinto menu
lista_de_entradas.append(clicked5) # Se agrega la opcion elegida a la lista de entradas

# Se crea un texto, correspondiente al titulo
text1 = tk.Label(root, text = "Bienvenido al buscador de canciones.", bg = "#1a9e8f", fg = "white", font = 10)
text1.place(relx = 0.01, rely = 0.03) # Se ajusta el tamaño y posicionamiento del texto
# Se crea un texto, correspondiente al subtitulo
text2 = tk.Label(root, text = "Seleccione sus preferencias y gustos.", bg = "#1a9e8f", fg = "white", font = 10)
text2.place(relx = 0.3, rely = 0.03) # Se ajusta el tamaño y posicionamiento del texto
text3 = tk.Label(root, text = "Atributos a elegir: ", bg = "#1a9e8f", fg = "white", font = 5)
text3.place(relx = 0.74, rely = 0.20) # Se ajusta el tamaño y posicionamiento del texto
text4 = tk.Label(root, text = "1. Reconocimiento del artista", bg = "#1a9e8f", fg = "white", font = 5)
text4.place(relx = 0.74, rely = 0.25) # Se ajusta el tamaño y posicionamiento del texto
text5 = tk.Label(root, text = "2. Duracion de la cancion", bg = "#1a9e8f", fg = "white", font = 5)
text5.place(relx = 0.74, rely = 0.30) # Se ajusta el tamaño y posicionamiento del texto
text6 = tk.Label(root, text = "3. Decada de la cancion", bg = "#1a9e8f", fg = "white", font = 5)
text6.place(relx = 0.74, rely = 0.35) # Se ajusta el tamaño y posicionamiento del texto
text7 = tk.Label(root, text = "4. Solista o banda", bg = "#1a9e8f", fg = "white", font = 5)
text7.place(relx = 0.74, rely = 0.40) # Se ajusta el tamaño y posicionamiento del texto
text8 = tk.Label(root, text = "5. Caracteristicas extras", bg = "#1a9e8f", fg = "white", font = 5)
text8.place(relx = 0.74, rely = 0.45) # Se ajusta el tamaño y posicionamiento del texto

# Se crea un boton, correspondiente al boton de busqueda de canciones
boton = tk.Button(root, text="Buscar canciones", command = lambda:recivir())
boton.place(relx = 0.80, rely = 0.55) # Se ajusta el tamaño y posicionamiento del boton

# Se crea una scrollbar, para asi poder ver mas resultados en caso de que sean muchos
barra = tk.Scrollbar(root, command = listbox.yview)
barra.place(relx = 0.71, rely = 0.10) # Se ajusta el tamaño y posicionamiento de la scrollbar

root.mainloop() # Se ejecuta la interfaz grafica
