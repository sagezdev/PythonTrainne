import sys

with open('lorem_ipsum.txt', "r") as file:
    texto = file.read()

print(texto)
    
nroCaracteres = len(set(texto))
nroPalabras = len(set(texto.split()))
    
print(nroCaracteres)
print(nroPalabras)
    