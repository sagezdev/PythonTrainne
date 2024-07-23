count = 0
sumaNota = 0
print('Bienvenido a tu portal')
while count < 5:
    nota = float(input('Ingrese su nota: '))
    sumaNota = nota + sumaNota
    count = count + 1
    if(count == 4):
        porcentaje = float(input('Ingresa tu % de asistencia: '))
        totalNota = sumaNota / 4
        if(totalNota > 4 and porcentaje > 75):
            print(f'Feliciades pasaste el curso con una nota de: {totalNota} y %{porcentaje} de asistencia fue')
        elif(totalNota < 4 and porcentaje > 75):
            print(f'Reprobaste por tu nota fue un: {totalNota}')
        elif(totalNota > 4 and porcentaje < 75):
            print(f'Reprobaste por tu % de asistencia: {porcentaje}')
        else:
            print(f'Sigue participando tu nota final fue:{totalNota}  y %{porcentaje} de asistencia fue')
