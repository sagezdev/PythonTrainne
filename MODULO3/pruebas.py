print('NORMAL')
animales = {'leon','gato','pantera','perro'}
print(animales)

print('ADD laika')
animales.add('Laika')
print(animales)

print('Update botas , lulu ')
animales.update(['botas','lulu']) 
print(animales)

print('Update 2 limon')
animales.update(['limon']) 
print(animales)


st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st1.update(st2)
print(st1)