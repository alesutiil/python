my_string = 'Mi string'
my_other_string = 'Mi otro string'

print(len(my_string))

print(my_string + "" + my_other_string)

my_new_line_string = 'String con\nsalto de línea'
print(my_new_line_string)

my_tab_string = '\tString con tabulación'
print(my_tab_string)

name, surname, age = 'Ale', 'Sutil', 24
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) # Esto es lo recomendable si estamos formateando
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')


# División

language = 'python'
language_slice = language[1:3] # Sin incluir la última
language_slice = language[1:] # Desde el caracter marcado hasta el final
print(language_slice)


# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize()) # Primera en mayúsculas
print(language.upper()) # Todo en mayúsculas
print(language.count('t')) # Cuenta 
print(language.isnumeric()) # Es un número?