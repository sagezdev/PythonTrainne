from medicamento import Medicamento

precio = int(input('Ingrese el precio:'  ))
es_valido = Medicamento.validar_mayor_a_cero(precio)

m1 = Medicamento()
m1.nombre = "Paracetamol"

if es_valido:
    print("Precio del micamento es valido")
    m1.precio = precio
else:
    print('Precio Malo')

print(m1.definicion())
print(m1.definicion2())