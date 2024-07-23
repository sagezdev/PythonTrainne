'''
    ingrese 4 notas
    ingrese % 

    obtener el promedio de > 4.0
    obtener la asistencia > 75%
'''

nota1 = float(input('Ingrese su primera nota: '))
nota2 = float(input('Ingrese su segunda nota: '))
nota3 = float(input('Ingrese su tercera nota: '))
nota4 = float(input('Ingrese su ultima nota: '))

porcentaje = float(input('ingrese el porcentaje de asistencia: '))


# se suma  el total de notas y se divide por 4 
sumaNotas = nota1 + nota2 + nota3 + nota4
totalNotas = sumaNotas / 4 

if(totalNotas > 4 and porcentaje > 75):
    print('Felicidades pasaste el curso')
else:
    print('No pudiste pasar el curso.. vuelvo a intetar mas tarde')