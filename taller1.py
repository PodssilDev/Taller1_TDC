# BLOQUE DE IMPORTACIONES
import sys
from pyswip import Prolog

prolog = Prolog()
prolog.consult("base.pl")

respuesta1 = input("Ingrese la duracion de la cancion: ")
respuesta2 = input("Exponente o Underground?: ")
respuesta3 = input("Ingrese una caracteristica extra: ")

if respuesta1 == "corta":
    parametro1 = "corta"
elif respuesta1 == "normal":
    parametro1 = "normal"
else:
    parametro1 = "larga"

consulta = list(prolog.query("song(J,_,exponente," + parametro1 + ", L)"))
if consulta == []:
    print("true")
else:
    print("false")
    print(consulta[0])

# Primero realizar las consultas, procurarse que funcione sin interfaz
# Luego, realizar las consultas con interfaz