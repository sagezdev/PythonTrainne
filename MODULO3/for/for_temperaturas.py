
from statistics import mean

count = 0
n_temp = int(input('Cuantas temperatuas desea agregar: '))
temperatura = [float(input(f'Ingrese una temperatura: ')) for i in range(n_temp)]

#Suma temperatura
sum_temperatura = sum(temperatura)
#Promedio temperatura
promedio_temperatura = round(sum_temperatura / n_temp,1)

#Sumar la temperatur y sacar el promedio pero de mejor forma
###promedio_celsius = round(mean(temperatura))
#Min temp , Max temp
min_temp , max_temp = min(temperatura), max(temperatura)
#Conversion de fahrenheit
fahrenheit = [round((celsius * 1.8) + 32,1) for celsius in temperatura]

for i in fahrenheit:
    print(f'La temperatura f es de : {i}  , las celsius es de: {temperatura[count]}')
    count += 1

print(f'El promedio de temperatura es de {promedio_temperatura}')
print(f'La temperatura ingresada es: {min_temp}. La maxima es de: {max_temp}')


