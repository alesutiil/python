import random

maquinaOpciones = ['piedra', 'papel', 'tijera']  

aleatorio = random.choice(maquinaOpciones)

maquina = aleatorio

persona = input('Eliges piedra, papel o tijera?\n')

if maquina == persona:
    print('empate')
elif persona == 'piedra' and maquina == 'tijera':
    print('ganaste, la máquina sacó tijera')
elif persona == 'papel' and maquina == 'piedra':
    print('ganaste, la máquina sacó piedra')
elif persona == 'tijera' and maquina == 'papel':
    print('ganaste, la máquina sacó papel')
else:
    print('perdiste, la máquina sacó ' + maquina)