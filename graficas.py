from importlib.metadata import distribution
import nltk
import matplotlib.pyplot as plt
carpeta_nombre = "C:\\Users\\jonya\\Desktop\\Pythonpln\\documentos\\"
archivo_nombre = "textolargo.txt"
with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

print(".................................................................")
tokens = nltk.word_tokenize(texto, "spanish")

tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk = nltk.Text(tokens)
distribution = nltk.FreqDist(texto_nltk)
print("...................................................................")

hapaxes = distribution.hapaxes()
for hapax in hapaxes:
    print(hapax)
from matplotlib import RcParams
RcParams.update({"figure.autolayout": True})
distribution.plot(cumulative = True)
distribution.plot(40, cumulative = True)

