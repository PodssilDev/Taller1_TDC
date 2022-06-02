# BLOQUE DE DEFINICIONES
# BLOQUE DE IMPORTACIONES
import sys
from pyswip import Prolog

# BLOQUE PRINCIPAL
prolog = Prolog()
prolog.consult("base.pl")

respuesta_1 = input("¿Prefiere un artista Exponente o Underground?: ")
respuesta_2 = input("¿Prefiere una cancion larga, corta o media?: ")
respuesta_3 = input("¿Prefiere una cancion de antes o despues de la decada de los 2000?:")
respuesta_4 = input("Prefiere una banda o un cantante en solitario?:")

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

if respuesta_3 == "antigua":
    moderna_antigua = "antigua"

else:
    moderna_antigua = "moderna"

if respuesta_4 == "banda":
    solitario_grupo = "banda"
else:
    solitario_grupo = "cantante"

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

if lista_respuestas == []:
    print("No hay respuestas")
else:
    if(no_encontrado == True):
        print("No se encontraron canciones con las caracteristicas elegidas, pero los siguientes son similares: ")
    else:
        print("Se encontraron las siguientes canciones: ")
    for respuesta in lista_respuestas:
        print(respuesta["Cancion"])


# Primero realizar las consultas, procurarse que funcione sin interfaz
# Luego, realizar las consultas con interfaz