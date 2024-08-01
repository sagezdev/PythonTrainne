def factorial(n):
    valor = 1
    for i in range(1, n+1):
        valor *= i
    return valor

def productoria(lista):
    valor = 1
    for i in lista:
        valor *= i
    return valor

def calcular(**kwargs):
    for k,v in kwargs.items():
        if 'fat' in k:
            return 'El factorial de ' , v , 'es: ' , factorial(v)
        else:
            return 'La productoria de ' , v , 'es: ' , factorial(v)
            
print(factorial(5))
print(productoria([4,5,6]))    
print(calcular(fact_1=5, prod_1 = [3,6,4,2,8], fact_2 = 6))