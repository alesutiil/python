my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print('La condición es mayor o igual que 10')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecución')
        break

    print(my_condition)



my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)


my_other_dict = {
    "Nombre": "Alejandro",
    "Apellido": "Sutil",
    "Edad": 24,
    "Lenguajes": {"Python", "HTML", "JavaScript"}
}

for element in my_other_dict:
    print(element)
    if element == "Apellido":
        break
        # continue
else:
    print('El bucle finaliza')