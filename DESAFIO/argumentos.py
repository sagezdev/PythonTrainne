import sys

nombre = sys.argv[1]
apellido = sys.argv[2]

print(type(sys.argv))
print(f'Mi nombres es {nombre}')
print(f'Mi apellido es {apellido}')
print(f'nombre de archivo es : {sys.argv[0]}')