def calcular_imc(peso, estatura):
    categoria = ""
    
    imc = round(peso / (estatura**2),1)
    
    if(imc < 18.5):
        categoria = "Bajo peso"
    elif(imc < 25):
        categoria = "Normal"
    elif(imc < 30):
        categoria = "Sobre Peso"
    else:
        categoria = "Obesidad"
        
    return categoria,imc




p = float(input('Ingreso su peso'))
e = float(input('Ingreso su estatura'))

estado , valor_imc = calcular_imc(p,e)
print(f'{p},{e}')
print(f'{valor_imc},{estado}')