count = 0
sumaNota = 0
situacion = ""
print('Bienvenido a tu portal')
while count < 4:
    nota = float(input('Ingrese su nota: '))
    sumaNota = nota + sumaNota
    count = count + 1
    if(count == 4):
        porcentaje = float(input('Ingresa tu % de asistencia: '))
        totalNota = round(sumaNota / 4, 1)
        if(totalNota > 4 and porcentaje > 75):
            situacion = 'Aprobado'
        elif(totalNota < 4 and porcentaje > 75):
            situacion = 'Reprobado por Nota'
        elif(totalNota > 4 and porcentaje < 75):
           situacion = 'Reprobado por porcentaje'
    else:
        situacion = 'Sigue participando'
        
print(f'{situacion}, Nota: {totalNota} , Asistencia: {porcentaje}')