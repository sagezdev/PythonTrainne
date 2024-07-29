the_list_str = ['js','html','css','react','ts','tailwind']
the_list_number = [1,5,7,23,9,2,4,6,3,4,2]
the_list_random = [2,'PYTHON',4,1,'Django','10',1,2,'MY SQL',5.5]


#Aqui setiamos y colocamos con un set para que se agrupen y no se repitan los numeros 
#Tambien le hacemos la funcion lis() ya que si solo ocupamos set esto devuelve un diccionario {}
lista_complet =  list(set(the_list_random + the_list_random))

#Esta lista solo devuelve los numeros enteros
list_comprimida = [num for num in lista_complet if type(num) == int or type(num) == float]

#y luego para sumar
print(list_comprimida)

