estimulos = input('Responde a estimulos [s|n]')

if estimulos == 's':
    print('valora la necesidad de llevarlo al hospital mas cercano')
else:
    print('Abrir la via aeria')
    respira = input('Respira [s|n]?')
    if('respira' == 's'):
        print('Permitirle posicion de suficiente ventilacion')
    else:
        print('administrarle 5 ventilaciones y llamar ambulacina.')
        contador_ventilaciones = 0
        while True:
            contador_ventilaciones += 1
            signos = input('Tiene signo de vida [s|n]: ')
            if(signos == 's'):
                print('Reevaluar a la espera de la ambulancia')
            else:
                print('administre compresiones toraxicas hasta que llegue la ambulancia')
            ambulancia = input('Llego la ambulacia [s|n]')
            if(ambulancia == 's'):
                break
            if contador_ventilaciones == 5:
                print('lo sentimos pero no podemos apoyarle mas..')
            
print('Gracias por seguir nuestras instrucciones y no permitir la muerte abrupta y dolorosa de una persona..')