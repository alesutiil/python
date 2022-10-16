# Un set NO es una estructura ordenada



# Formas de definir sets
my_set = set()
my_other_set = {}

my_other_set = {'Hola', 'Ale', 24}

print(len(my_other_set))

# print(my_other_set[2]) Esto daría error ya que es desordenado por lo que no podemos acceder a su índice

my_other_set.add('Sutil')
print(my_other_set)

my_other_set.add('Sutil') # Un set no admite repetidos
print(my_other_set)

# Búsqueda
print('Ale' in my_other_set)
print('Alex' in my_other_set)

my_other_set.remove('Hola')
print(my_other_set)

my_set = {'Hola', 'Jamón'}

my_new_set = my_set.union(my_other_set) # Unimos dos sets
print(my_new_set)

print(my_new_set.difference(my_set)) # De my_new_set le quitamos lo que aparece en my_set