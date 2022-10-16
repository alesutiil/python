# Manejo de errores

from multiprocessing.sharedctypes import Value


numberOne = 5
numberTwo = 1
numberTwo = "1"


# try except (siempre obligatorio)

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')


# try except else

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')
else: # Si se produce un except no se produce
    print('Seguimos...')


# try except else finally

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')
else: # Si se produce un except no se produce
    print('Seguimos...')
finally: # Se ejecuta siempre
    print('La ejecución sigue')



# Excepciones por tipo

print('-------------------------')

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')



# Captura de la información de la excepción

print('-------------------------')

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error:
    print(error)
except Exception as error:
    print(error)
