# Formas de definirlo
my_dict = dict()
my_other_dict = {}

my_other_dict = {
    "Nombre": "Alejandro",
    "Apellido": "Sutil",
    "Edad": 24,
    "Lenguajes": {"Python", "HTML", "JavaScript"}
}
print(my_other_dict)
print(my_other_dict["Apellido"])

my_other_dict["Calle"] = "Calle Pepito" # Añadimos un nuevo valor
print(my_other_dict)

del my_other_dict["Calle"] # Eliminar un valor del diccionario
print(my_other_dict)

print("Sutil" in my_other_dict) # False porque no mira valor
print("Nombre" in my_other_dict) # True porque mira clave
print("Sutil" in my_other_dict["Apellido"]) # True

print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

my_new_dict = dict.fromkeys(("Nombre", "Edad", "Piso")) # Crea un nuevo diccionario
print(my_new_dict)

my_list = ['Nombre', 'Edad', 'Piso', 'Otra clave']
my_new_dict = dict.fromkeys(my_list) # Crea un nuevo diccionario a partir de una lista
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict) # Crea un nuevo diccionario a partir de otro
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict, ("Jeje")) # Crea un diccionario con el mismo valor para todas las claves
print(my_new_dict)