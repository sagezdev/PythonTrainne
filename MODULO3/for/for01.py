notas = []
acumNotas = 0

for i in range(5):
    nota = float(input(f'Ingrese nota {i + 1}: '))
    notas.append(nota)

for data in notas:
    acumNotas += nota
    
promedio = round(acumNotas / len(notas),1)

situacion = ['Aprobado' if nota >= 4 else 'Reprobado' for nota in notas]

'''
for nota in notas:
    if nota >= 4:
        situacion.append('Aprobado')
    else:
        situacion.append('Reprobado')
'''

for i in range(len(notas)):
    print(f'{notas[i]} | {situacion[i]}')
    
print(f'Promedio curso: {promedio}')