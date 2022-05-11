print("Procesamiento de lenguaje natural")
print("Ingeniería en computación inteligente")
suma = 7+5
resultado = suma*6
print("resultado = ",resultado)
print("________________________________________")
archivo=open("C:\\Users\\jonya\\Desktop\\Pythonpln\\archivo.txt")
print(archivo.read())
archivo.close()

print("_________________________________________")
archivo2=open("C:\\Users\\jonya\\Desktop\\Pythonpln\\archivo1.txt","w")
cadena1 = "primer clase de programacion python, en procesamiento"
archivo2.write(cadena1)
archivo2=open("C:\\Users\\jonya\\Desktop\\Pythonpln\\archivo1.txt")
print(archivo2.read())
archivo2.close()