'''
Manejo de except con un try except
'''

while True:
    try:
        nota = float(input('Ingrese una nota entre 1.0 y 7.0'))
        if(nota < 1 or nota >7):
            print('nota no es valida Debre ingresar una nota entre 1.0 y 7.0')
        else:
            break
    except ValueError:
        print('El valor ingresado no es un numero')
