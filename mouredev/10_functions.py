def my_function ():
    print('Esto es una función')

my_function()


def sum_two_values(param_one, param_two):
    print(param_one + param_two)

sum_two_values(1,2)


def sum_two_values_with_return(firts_value, second_value):
    return firts_value + second_value

my_result = sum_two_values_with_return(2,4)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name('Ale', 'Sutil')
print_name(surname = 'Sutil', name = 'Ale')


def print_name_with_default (name, surname, alias = "Este es mi valor por defecto"):
    print(f"{name} {surname} {alias}")

print_name_with_default('Ale', 'Sutil')



# Función con parametros arbitrarios
def print_texts(*text):
    print(text)

print_texts('Hola', "Adiós")

def print_upper_texts(*text):
    for text in text:
        print(text.upper())

print_upper_texts('Hola', "Adiós", "Sutil")