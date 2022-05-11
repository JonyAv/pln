from importlib.metadata import distribution
from typing import Text
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

frecWords = distribution.most_common(20)
print(frecWords)
print(texto_nltk.generate())
texto_nltk.dispersion_plot(['las', 'en', 'de', 'como'])