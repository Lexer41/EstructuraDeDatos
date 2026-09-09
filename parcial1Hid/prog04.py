# Hacer un programa que lea un numero y que muestre el dia de la semana
# que representa

a = int(input('Escribe un numero '))

if a == 1:
    print('Es lunes')
elif a == 2:
    print('Es martes')
elif a == 3:
    print('Es miercoles')
elif a == 4:
    print('Es Jueves')
elif a == 5:
    print('Es viernes')
elif a == 6:
    print('Es sabado')
elif a == 7:
    print('Es domingo')
else:
    print('Numero no corresponde a ningun dia')