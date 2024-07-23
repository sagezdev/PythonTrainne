import random

opcionesComputador = random.randint(1,3)
print("[1] Piedra")
print("[2] Papel")
print("[3] Tijera")
opcion = int(input('ingresa tu opcion ganadora: '))

mensaje = ""
selecionJugador = ""
seleccionPc = ""

if(opcion < 4):
    if(opcionesComputador == 1 and opcion == 2):
        mensaje = "Ganaste"
        seleccionPc = "piedra"
        selecionJugador = "papel"
    elif(opcionesComputador == 1 and opcion == 3):
        mensaje = 'Perdiste'
        seleccionPc = 'piedra'
        selecionJugador = 'Tijera'
    elif(opcionesComputador == 2 and opcion == 1):
        mensaje = 'Perdiste'
        seleccionPc = 'Papel'
        selecionJugador = 'Piedra'
    elif(opcionesComputador == 2 and opcion == 3):
        mensaje = 'Ganaste'
        seleccionPc = 'Papel'
        selecionJugador = 'Tijera'
    elif(opcionesComputador == 3 and opcion == 1):
        mensaje = 'Ganaste'
        seleccionPc = 'Tijera'
        selecionJugador = 'Piedra'
    elif(opcionesComputador == 3 and opcion == 2):
        mensaje = 'Perdiste'
        seleccionPc = 'Tijera'
        selecionJugador = 'Piedra'
    else:
        mensaje = 'Empate'
        
    if( mensaje != 'Empate'):
        print(f'jugador: {selecionJugador} vs Pc: {seleccionPc} Resultado:{mensaje}')
    else:
        print('Empate')
        
else:
    print(f'ERROR tu opcion {opcion} no es valida ingresa un numero del 1 al 3')


