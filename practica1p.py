'''
Jonathan Guadalupe Alvarado Vargas
- el programa consiste en leer dos documentos de texto.txt
- cada documento de texto.txt debe de tener tres parrafos como minimo,
- de los cuales muestre cuantas lineas(longitud) con texto y
- cuantas lineas vacias tiene cada documento,
- que elimine los simbolos de puntuacion y
- que muestre todas las palabras que contiene cada documento de manera ordenada,
- que muestre cuantas palabras(longitud) contiene cada documento,
- que una los dos documentos en otro nombre de documento.txt y que elimine los simbolos
- de puntuacion y que muestre todas las palabras que contiene el documento nuevo
- de manera ordenada y que muestre cuantas palabras(longitud) contiene el documento,
- que escribas una palabra y la busque e indique si la encontro o no

'''

import os

carpeta_nombre = "C:\\Users\\jonya\\Desktop\\Pythonpln\\documentos\\"
carpeta_salida = "C:\\Users\\jonya\\Desktop\\Pythonpln\\documentos\\"

archivo_salida = "UNIONp1.txt"

archivos_lista = os.listdir(carpeta_nombre)

for archivo_nombre in archivos_lista:
    print("\n\n\n |..................NOMBRE DE ARCHIVO...................|")
    print("\n Nombre archivo: ", archivo_nombre)
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_lista= archivo.readlines()

    num_palabras = 0
    num_linea = 0
    num_texto = 0
    num_vacio = 0
    for linea in lineas_lista:
        if linea.strip() == "":
            num_linea = num_linea + 1
            num_vacio = num_vacio + 1

        else:
            num_linea = num_linea + 1
            num_texto = num_texto + 1

    print("\n |.........LINEAS TOTALES...........|")
    print("Lineas totales: ", num_linea)
    print("\n |........LINEAS CON TEXTO.........|")
    print("Lineas con texto: ", num_texto)
    print("\n |........LINEAS VACIAS............|")
    print("Lineas vacias: ", num_vacio)          


    archivo = open(carpeta_nombre+archivo_nombre)
    texto = archivo.read()
    archivo.close()

    simbolos = ["(", ")", ",", ".", ";", ":", "/", "\""]
    for simbolo in simbolos:
        texto = texto.replace(simbolo," ")
    
    palabras_lista = texto.split()
    palabras_lista.sort()
    print("\n |........LISTA DE PALABRAS ORDENADAS.........|")
    for words in palabras_lista:
        print(words)

    longitud_words = len(palabras_lista)
    print("\n |........NÚMERO TOTAL DE PALABRAS.........|")  
    print("Numero de palabras de todo el documento: ", longitud_words)





union = ""
for archivo_nombre in archivos_lista:
    archivo = open(carpeta_nombre + archivo_nombre)
    texto_u = archivo.read()
    archivo.close()
    union += texto_u

    with open(carpeta_salida + archivo_salida, "w") as salida:
        salida.write(union)

print("\n\n\n |..................NOMBRE DE ARCHIVO...................|")
print("\n Nombre archivo: ", archivo_salida)      

simbolos = ["(", ")", ",", ".", ";", ":", "/", "\""]
for simbolo in simbolos:
    texto_u = texto_u.replace(simbolo," ")
    
palabras_listau = texto_u.split()
palabras_listau.sort()

print("\n |........LISTA DE PALABRAS ORDENADAS........|")
for words_u in palabras_listau:
    print(words_u)

long_words = len(palabras_listau)
print("\n |.......NÚMERO TOTAL DE PALABRAS.........|")  
print("Numero de palabras de todo el documento: ", long_words)
    
print("\n |.......BÚSQUEDA DE PALABRAS..........|") 
palabra = input("\n Escribe la palabra a buscar en el documento: ")
if palabra in palabras_listau:
    num_palabras = num_palabras + 1
    print("La palabra: ", palabra, "SI se encontró en el texto")
    print("La palabra: ", palabra, "se encuentra: ", num_palabras, "veces en el texto")
else:
    print("La palabra: ", palabra, "NO se encontró en el texto")
    