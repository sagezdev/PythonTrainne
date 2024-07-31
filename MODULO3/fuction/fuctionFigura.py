from math import sqrt

def fuctionFigura(a,b):
    #Perimetro
    perimetro = 2*(a+b)
    #Area
    area = a * b
    
    #Diagonal 
    diagonal = round(sqrt(a**2 + b**2),1) 

    return  perimetro,area,diagonal

area_a = float(input('Ingrese el lado a: '))
area_b = float(input('Ingrese el lado b: '))

(perimetro, area, diagonal) = fuctionFigura(area_a,area_b)

print('\f')
print(f'El perimetro es: {perimetro} \nEl area es {area}\nLa diagonal es: {diagonal}')