'''
filtrar a solo los mayores de edad, obteniendo el promedio
'''

promedio = 0
sumMayor = 0
edades = [int(input('Ingresa tu edad: ')) for i in range(10)]

for mayores in edades:
    if(mayores >= 18):
        sumMayor += mayores
        print(sumMayor)
        promedio = round(sumMayor / len(edades),1)

maMin = [ 'Mayor de edad' if edad >= 18 else 'Menor de edad' for edad in edades  ]

for i in range(len(edades)):
    print(f'Edad:{edades[i]} | Rango:{maMin[i]} ')
    
print(f'Promedio de los mayores de edad: {promedio}')