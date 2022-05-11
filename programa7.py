import re
carpeta_nombre = "C:\\Users\\jonya\\Desktop\\Pythonpln\\documentos\\"
archivo_nombre = "texto2.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()
expresion_regular = re.compile(r"cumplir")

resultados_busqueda = expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular = re.compile(r"la+")
resultados_busqueda = expresion_regular.finditer(texto)
for resultado1 in resultados_busqueda:
    print(resultado1.group(0))