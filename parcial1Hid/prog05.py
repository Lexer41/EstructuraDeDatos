# Estructuras

#a = "hola mundo"

#for i in a:
#    print(i)

#for i in range(1, 5):
#    print(i)

#a = 1
#while(a <= 5):
    #print("hola mundo")
    #a = a + 1
    #a += 1


# Hacer un programa que lea 10 numeros y que muestre en pantalla la suma de ellos
# con for

'''
suma = 0

for x in range(1, 11):
    a = int(input("Escribe un numero \n"))
    suma += a

print(f'La suma de los numeros son {suma}')
'''
x = 1
suma = 0

while (x <= 5):
    a = int(input("Escribe un numero: "))
    x += 1
    suma += a

print(f'La suma de los numeros son {suma}')