#Crear un arreglo del 1 al 10
#E imprimir solo los elementos pares


numbers = [1,2,3,4,5,6,7,8,9,10]

print ("solo los números pares")
for number in numbers:
   if number % 2 == 0:
    print(number) 

print ("solo los números impares")
for number in numbers:
    if number % 2 != 0:
     print(number)
