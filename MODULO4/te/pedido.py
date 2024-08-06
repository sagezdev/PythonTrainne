from te import Te
sabor = int(input('***\nQue sabor de te deseas?\n[1] Te negro\n[2] Te verde\n[3] Te de hierbas\n>>> '))
formato = int(input('***\nQue formato deseas llevar tu Te?\n[1] 300gr\n[2] 500gr\n>>> '))

nombre,tiempo, recomendacion = Te.tiempo_recomendacion(sabor)
precio = Te.obtener_precio(300 if formato == 1 else 500)

print(f'El {nombre} de {300 if formato == 1 else 500}gr\nEs recomenado: {recomendacion}\nEl tiempo de preparacion es de: {tiempo} min\nMonto a pagar ${precio} pesos')

