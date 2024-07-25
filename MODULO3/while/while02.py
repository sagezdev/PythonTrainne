acumNotas = 0
cNotas = 0

while True:
    while True:
        try:
            nota = float(input(f'Ingrese {cNotas + 1} nota entre 1.0 y 7.0: '))
            if(nota < 1 or nota >7):
                print('nota no es valida Debre ingresar una nota entre 1.0 y 7.0')
            else:
                break
        except ValueError:
            print('El valor ingresado no es un numero')

    cNotas += 1
    acumNotas += nota
    
    while True:
        resp = input('Desea agregar una nueva nota Si[S] o No[N]')
        if(resp.lower() != 's' and resp.lower() != 'n'):
            print('Respuesta incorrecta tiene que ser un [s] o [n]')
            print('----------------------------------------------')
        else:
            break
        
    if(resp.lower() == 'n'):
        break
    
promedio = round(acumNotas / cNotas,1)
print(f'Su promedio es de {promedio}')
