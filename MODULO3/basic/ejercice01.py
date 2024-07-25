nombre = input('Ingresa tu nombre')
notaFinal = float(input('Ingrese su nota final'))
clasificacion = ''

# El proceso en este caso sera cuando haga sus comparaciones
if notaFinal < 3: 
    clasificacion = 'Verguenza para la humanidad'
elif notaFinal < 4:
    clasificacion = 'Penosos pero con opciones'
elif notaFinal < 5:
    clasificacion = 'Reguleque'
elif notaFinal < 6: 
    clasificacion = 'Del monton'
elif notaFinal < 7:
    clasificacion = 'Brillante'
else:
    clasificacion = 'Genio'

print(f'{nombre},segun tu notal final ({notaFinal}) tu clasificacion es: {clasificacion}')