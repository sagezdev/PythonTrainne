from orden_compra import Orden_compra
oc = Orden_compra()
oc.nueva_orden()

oc.identificor = int(input('Ingrese el identificador de la OC:\n'))
oc.total_productos = int(input('Ingrese el total de productos:\n'))
monto = int(input('Ingrese el monto:\n'))

oc.asgina_monto(monto)

if(oc.monto > 20000):
    oc.codigo_descuento = "20PORCIENTO"
elif(oc.monto > 10000):
    oc.codigo_descuento = "10PORCIENTO"
    
print(oc.codigo_descuento)
