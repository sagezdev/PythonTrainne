
import sys
umbral = float(sys.argv[1])

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar(diccionario, umbral, mayor_que = True):
    if(mayor_que):
        filtro = [k for k , v in diccionario.items() if v > umbral]
    else:
        filtro = [k for k , v in diccionario.items() if v < umbral]
        
    return filtro

if len(sys.argv) == 2:
    print(f'Los productos mayores al umbral son: {', '.join(filtrar(precios,umbral)) }')
else:
    if(sys.argv[2] == 'mayor'):
        print(f'Los productos mayores al umbral son:{', '.join(filtrar(precios,umbral,True))}')
    elif(sys.argv[2] == 'menor'):
        print(f'Los productos menores al umbral son:{', '.join(filtrar(precios,umbral,False))}')
    else:
        print('Operacion Incorrecta')
        