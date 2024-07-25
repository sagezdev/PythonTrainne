import random

numeros = [random.randint(1,50) for i in range(10)] #listaa x comprension

'''
for i in range(10):
    numeros.append(random.randint(1,50))
'''

situacion = ['par' if numero % 2 == 0 else 'impar' for numero in numeros]

    
for i in range(len(numeros)):
    print(f'{numeros[i]} \t {situacion[i]}')
    
pares = [numero for numero in numeros if numero % 2 == 0]
print(sorted(pares,reverse=True))
pares.sort()
print(pares)