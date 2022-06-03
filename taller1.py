# BLOQUE DE DEFINICIONES
# BLOQUE DE IMPORTACIONES
import sys
from pyswip import Prolog
from statistics import mode

# BLOQUE DE FUNCIONES

def mas_repetido(lista_generos):
    return(mode(lista_generos))

# BLOQUE PRINCIPAL
prolog = Prolog()
prolog.consult("base.pl")

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

if respuesta_3 == "antigua":
    moderna_antigua = "antigua"

else:
    moderna_antigua = "moderna"

if respuesta_4 == "banda":
    solitario_grupo = "banda"
else:
    solitario_grupo = "cantante"

'''
La idea es que esta pregunta permita determinar con certeza el GENERO preferido
No lo coloque aun en la base de conocimiento ya que faltan aun colocar las respuestas
de algunos generos. Por mientras lo dejo asi por si alguien queire avanzar en algo mas
Sigo apenas llegue a casa

if respuesta_5 == "Que tenga letras de amor": # Romantica
    caracteristica = "letras_amor"

elif respuesta_5 == "Que tenga guitarras fuertes y distorcionadas": # Metal
    caracteristica = "guitarras_fuertes"

elif respuesta_5 == "Que tenga una preferencia por la artesania y diversos elementos": # POP
    caracteristica = "artesania"

elif respuesta_5 == "Que tenga sonidos electronicos": # Electronica
    caracteristica = "sonidos_electronicos"

elif respuesta_5 == "Que provoque querer bailar": # Disco
    caracteristica = "querer_bailar"

elif respuesta_5 == "Que contenga una letra hablada rapidamente": # Hip-Hop
    caracteristica = "letras_rapidas"

elif respuesta_5 == "Que tenga una letra en tono medio y una guitarra electronica":
    caracteristica = "tono_medio"
 
elif respuesta_5 == "Que tenga sonidos de saxophone": # Jazz
    caracteristica = "sonidos_saxophone"


Pop LISTO
Metal LISTO
Disco LISTO
Hip-Hop LISTO
Romantico LISTO
Rock LISTO
Jazz LISTO
Blues
Rock n Roll
Country
Techno
Salsa
Reggae
Clasica
Cumbia
Electronica LISTO
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

# Primero realizar las consultas, procurarse que funcione sin interfaz
# Luego, realizar las consultas con interfaz
