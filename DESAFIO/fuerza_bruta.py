import getpass
from string import ascii_lowercase as abc

pass_user =  getpass.getpass('Ingrese su password: ')
intentos = 0
contadorValidacion = 0

for i in range(len(abc)):
    for a in range(len(pass_user)):
        intentos += 1
        if(abc[i] == pass_user[a]):
            print(f'\n-------------')
            print(f'[{abc[i]}] numero de intentos fue: {intentos}')
            contadorValidacion += 1
            break
        
if(contadorValidacion == len(pass_user)):
    print(f'\n----------------')
    print('Logramos forzar la password exitosamente')
else:
    print('No logramos forzar tu pass')
    