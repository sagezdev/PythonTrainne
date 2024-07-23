import math

peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))
mensaje = ''

#FORMULA
imc = round(peso / math.pow(altura,2),2)

#CONDICIONAL
if imc < 18.5:
    mensaje = 'Bajo Peso'
elif imc < 25: 
    mensaje = 'Adecuado' 
elif imc < 30:
    mensaje = 'Sobrepeso'
elif imc < 35:
    mensaje = 'Obesidad grado 1'
elif imc < 40:
    mensaje = 'Obesidad grado 2'
else:
    mensaje = 'Obesidad grado 3'

print(f'Su estado nutricional es de: {mensaje}')