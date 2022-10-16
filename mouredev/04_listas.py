# La lista es un conjunto de datos



# Forma de definirlas
my_list = list()
my_other_list = []


my_custom_list = [24, 1.90, 'Ale'] # Una lista no tiene por qué ser del mismo tipo de dato
print(my_custom_list[0])

age, height, name = my_custom_list
print(height)


otra_lista = [4, 33, 33, 12, 28, 65]
print(otra_lista.count(33)) # Retorna cuantas veces aparece el mismo valor en la lista


print(my_custom_list + otra_lista) # Sumamos dos listas


my_custom_list.append('Otro elemento') # Insertamos un elemento al final de la lista
print(my_custom_list)

my_custom_list.insert(1, 'Negro') # Inserta el elemento en la posición que indiquemos
print(my_custom_list)

my_custom_list.remove(1.90) # Elimina un elemento de la lista (si aparece mças de 1 vez el mismo elemento, elimina sólo el primero). Se usa para eliminar un elemento que ya conocemos
print(my_custom_list)

otra_lista.pop() # Elimina el último elemento de la lista (puedes indicar el índice que quieres eliminar)
print(otra_lista)

del otra_lista[3] # Eliminar por índice
print(otra_lista)

my_new_list = otra_lista.copy() # Copia una lista
print(my_new_list)

otra_lista.reverse() # Reverse
print(otra_lista)

otra_lista.sort() # Ordena
print(otra_lista)

print(otra_lista[1:2]) # Slice

otra_lista.clear() # Vacía la lista
print(otra_lista)