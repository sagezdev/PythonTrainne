def suma(*args):
    sumar = 0
  
    for i in args:
        if type(i) != int: return sum(i)

    for num in args:
        sumar = num + sumar
    return sumar

print(suma([1,23,4]))
print(suma(1,23,4))