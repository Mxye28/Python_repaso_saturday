import random
import time

#El módulo random tiene varias funciones para trabajar con números aleatorios.
#La función choice es una de las más usadas eligiendo un elemento al azar desde una lista

fruits = ['manzana','pera','frutillas', 'piña']

# Imprimir una fruta al azar
print('Redoble de tambores....')

for i in range(1,4):
    print(".")
    time.sleep(0.5)

print('tu fruta es: ')
print (random.choice(fruits))