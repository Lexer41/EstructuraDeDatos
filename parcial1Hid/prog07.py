# Hacer un programa que lea un numero correspondiente entre 1 y 9,
# acontinuacion realizara una pregunta indicando si desea introducir otro numero
# si la respuesta es si realizara nuevamente el proceso de lectura de datos,
# si la respuesta es no el programa mostrara laa suma, promedio y cantidad de numeros introducidos
# ademas de los numeros que se introdujeron 

c = 0
p = "s"
suma = 0
su = ""

while(p =="s" or p == "S"):
    a = int(input("Escribe un numero \n")) # Verificar que sea entre 1 y 9

    if a >= 1 and a <= 9:
        c += 1
        suma += a
        su += str(a)
        p = input("Deseas otro numero s/n \n")

        if p == "s" or p == "S":
            print("Se introducira otro numero")
        else:
            break
    else:
        print("El numero no esta entre 1 y 9 \n vuelve a intentarlo")

print(f"La suma de los numeros son {suma} y el promedio es {suma / c} \n y la cantidad de numeros son {c} \n y los numeros involucrados son {su}")