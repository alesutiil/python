# Las tuplas son inmutables



# Formas de definirla
my_tuple = tuple()
my_tuple = ()

my_other_tuple = (1, 'hola')


my_tuple = (24, 1.90, 'Ale')
print(my_tuple)

# my_tuple[1] = 20 Esto daría error porque las tuplas no se pueden modificar, son inmutables mientras que las listas si podemos

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:5])

my_tuple = list(my_tuple)
print(my_tuple)

my_tuple[1] = 20
print(my_tuple)

my_tuple = tuple(my_tuple)
print(my_tuple)

del my_tuple # Elimina la variable, no la vacía por lo tanto deja de estar definida