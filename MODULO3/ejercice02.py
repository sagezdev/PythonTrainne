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
situacion = ''
# se suma  el total de notas y se divide por 4 
sumaNotas = nota1 + nota2 + nota3 + nota4
totalNotas = round(sumaNotas / 4,1) 


if(totalNotas >= 4 and porcentaje >= 75):
    situacion = 'Felicidades aprobaste'
else:
    situacion = 'Reprobaste el curso'
    
print(f'Promedio: {totalNotas}')
print(f'Asistencia: {porcentaje}%')
print(situacion)