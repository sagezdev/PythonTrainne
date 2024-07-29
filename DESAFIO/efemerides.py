efemerides = {'1 de enero': 'Año Nuevo',
 '27 de febrero': 'Terremoto en Chile',
 '8 de marzo': 'Día de la Mujer',
 '21 de mayo': 'Glorias Navales',
 '18 de septiembre': 'Fiestas Patrias',
 '19 de septiembre': 'Glorias del Ejercito',
 '25 de diciembre': 'Navidad'}


fecha = input('Ingrese la fecha: ').lower()

print(f'Efemerides: {efemerides.get(fecha, 'No encontramos la fecha')}')

