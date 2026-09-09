# Hacer un programa que lea 4 numeros y calcule el promedio

a = int(input('Escribe un nuemro \n'))
b = int(input('Escribe otro nuemro \n'))
c = int(input('Escribe otro nuemro mas \n'))
d = int(input('Escribe un ultimo nuemro \n'))
promedio = (a + b + c + d) / 4

print(f'El promedio es: {promedio}')

if promedio >= 7:
    print('Si aprobo')
else:
    print('No aprobo')