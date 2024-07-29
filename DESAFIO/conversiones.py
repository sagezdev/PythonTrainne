import sys 
valor = sys.argv

peru = float(sys.argv[1])
argentina = float(sys.argv[2])
dolar = float(sys.argv[3])
chile = float(sys.argv[4])

#FORMULA 
formula_pe = peru * chile
formula_arg = argentina * chile
formula_dolar = dolar * chile

print(f'los {chile} pesos equivalen a: {formula_pe} soles: {formula_arg} pesos Arg: {formula_dolar} Dólares')

